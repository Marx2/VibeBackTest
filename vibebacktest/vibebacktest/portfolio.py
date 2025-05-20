class Portfolio:
    def __init__(self):
        self.holdings = {}

    def add_asset(self, asset, quantity):
        if asset in self.holdings:
            self.holdings[asset] += quantity
        else:
            self.holdings[asset] = quantity

    def remove_asset(self, asset, quantity):
        if asset in self.holdings:
            if self.holdings[asset] >= quantity:
                self.holdings[asset] -= quantity
                if self.holdings[asset] == 0:
                    del self.holdings[asset]
            else:
                raise ValueError("Not enough quantity to remove")
        else:
            raise KeyError("Asset not found")

    def update_holdings(self, transaction_type, asset, quantity):
        if transaction_type == 'buy':
            self.add_asset(asset, quantity)
        elif transaction_type == 'sell':
            self.remove_asset(asset, quantity)
        else:
            raise ValueError("Invalid transaction type")

    def get_total_value(self, prices):
        total = 0
        for asset, quantity in self.holdings.items():
            total += prices.get(asset, 0) * quantity
        return total
