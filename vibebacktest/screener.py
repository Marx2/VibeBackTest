# screener.py

import openbb
import yaml

class Screener:
    def __init__(self, strategy_file):
        self.strategy_file = strategy_file
        self.conditions = self._load_conditions()

    def _load_conditions(self):
        """Load screening conditions from the strategy YAML file."""
        with open(self.strategy_file, 'r') as file:
            strategy = yaml.safe_load(file)
        return strategy.get('conditions', {})

    def screen_stocks(self):
        """Fetch and filter stocks based on conditions."""
        try:
            # Fetch stock data using OpenBB API
            stocks = openbb.stocks.screener(self.conditions)
            
            # Apply filtering logic
            filtered_stocks = []
            for stock in stocks:
                match = all(
                    # Safer alternative to eval with operator mapping
                    operators = {
                        '>': lambda a, b: a > b,
                        '<': lambda a, b: a < b,
                        '>=': lambda a, b: a >= b,
                        '<=': lambda a, b: a <= b,
                        '==': lambda a, b: a == b,
                        '!=': lambda a, b: a != b
                    }
                    if cond['operator'] not in operators:
                        raise ValueError(f"Unsupported operator: {cond['operator']}")
                    if not operators[cond['operator']](stock.get(cond['metric'], 0), cond['value']):
                        match = False
                    for cond in self.conditions
                )
                if match:
                    filtered_stocks.append(stock)
            
            return filtered_stocks
        except Exception as e:
            print(f"Error during screening: {e}")
            return []