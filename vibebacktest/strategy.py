import yaml
import logging

def load_strategy(file_path: str) -> dict:
    """
    Load and validate a strategy configuration from a YAML file.

    Args:
        file_path (str): Path to the YAML configuration file.

    Returns:
        dict: Parsed and validated strategy configuration.

    Raises:
        ValueError: If the YAML file is invalid or missing required fields.
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    required_fields = {"asset_selection", "allocation_rules"}

    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file: {e}")

    if not isinstance(config, dict):
        raise ValueError("The configuration file must contain a valid dictionary.")

    missing_fields = required_fields - config.keys()
    if missing_fields:
    
        # Debugging: Log the parsed YAML content and missing fields
        logging.debug(f"Parsed YAML content: {strategy_config}")
        logging.debug(f"Missing fields: {missing_fields}")
        raise ValueError(f"The configuration file is missing required fields: {', '.join(missing_fields)}")

    return config

# Example usage
if __name__ == "__main__":
    try:
        strategy = load_strategy("sample_strategy.yaml")
        print("Loaded strategy:", strategy)
    except Exception as e:
        print(f"Error: {e}")
