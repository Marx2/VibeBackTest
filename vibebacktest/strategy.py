import yaml
import os

def load_strategy(file_path):
    """
    Load and validate the strategy YAML file.

    Args:
        file_path (str): Path to the strategy YAML file.

    Returns:
        dict: Parsed strategy configuration.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the YAML file is invalid or missing required fields.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Strategy file not found: {file_path}")

    with open(file_path, "r") as file:
        try:
            strategy = yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file: {e}")

    # Validate required fields
    required_fields = ["initial_capital", "monthly_addition", "rebalancing", "screener"]
    for field in required_fields:
        if field not in strategy:
            raise ValueError(f"Missing required field in strategy: {field}")

    # Extract and validate screener conditions
    screener_conditions = strategy.get("screener", {})
    if not screener_conditions:
        raise ValueError("Screener conditions are missing in the strategy file.")
    if not isinstance(screener_conditions, dict):
        raise ValueError("Screener conditions must be a dictionary.")

    # Add screener conditions to the strategy
    strategy["screener_conditions"] = screener_conditions

    return strategy