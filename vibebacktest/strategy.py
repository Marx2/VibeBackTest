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

    return strategy
import yaml

def load_strategy(file_path):
    """
    Load and validate a strategy configuration from a YAML file.
    """
    with open(file_path, 'r') as file:
        strategy = yaml.safe_load(file)
    
    # Validate required fields
    required_fields = ["name", "description", "parameters", "rules"]
    for field in required_fields:
        if field not in strategy.get("strategy", {}):
            raise ValueError(f"Missing required field: {field}")
    
    # Additional validation for parameters
    params = strategy["strategy"]["parameters"]
    if not (0 < params.get("lookback_period", 0) <= 365):
        raise ValueError("lookback_period must be between 1 and 365.")
    if not (0 <= params.get("oversold_threshold", 0) <= 100):
        raise ValueError("oversold_threshold must be between 0 and 100.")
    if not (0 <= params.get("overbought_threshold", 0) <= 100):
        raise ValueError("overbought_threshold must be between 0 and 100.")
    if not (0 < params.get("position_size", 0) <= 1):
        raise ValueError("position_size must be between 0 and 1.")
    
    return strategy