import yaml

def load_and_validate_strategy(file_path):
    """Load and validate strategy YAML file."""
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    
    # Check required fields
    required_fields = ['initial_capital', 'monthly_addition', 'rebalancing', 'screener']
    for field in required_fields:
        if field not in config:
            raise KeyError(f"Missing required field: {field}")
    
    # Validate initial_capital
    if not isinstance(config['initial_capital'], (int, float)) or config['initial_capital'] <= 0:
        raise ValueError("initial_capital must be a positive number")
    
    # Validate monthly_addition
    if not isinstance(config['monthly_addition'], (int, float)) or config['monthly_addition'] < 0:
        raise ValueError("monthly_addition must be a non-negative number")
    
    return config
