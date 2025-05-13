class Portfolio:
    """
    A class to manage a portfolio of assets with cash balance.
    """

    def __init__(self):
        """
        Initializes an empty portfolio with a cash balance of 0.
        """
        self.cash = 0.0
        self.assets = {}

    def add_cash(self, amount: float):
        """
        Adds cash to the portfolio.

        :param amount: The amount of cash to add.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Cannot add a negative amount of cash.")
        self.cash += amount

    def buy_asset(self, asset: str, quantity: int, price: float):
        """
        Buys an asset and updates the portfolio.

        :param asset: The name of the asset.
        :param quantity: The quantity of the asset to buy.
        :param price: The price per unit of the asset.
        :raises ValueError: If the quantity or price is negative.
        :raises ValueError: If there is insufficient cash to buy the asset.
        """
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive.")
        total_cost = quantity * price
        if total_cost > self.cash:
            raise ValueError("Insufficient cash to buy the asset.")
        self.cash -= total_cost
        if asset in self.assets:
            self.assets[asset] += quantity
        else:
            self.assets[asset] = quantity

    def sell_asset(self, asset: str, quantity: int, price: float):
        """
        Sells an asset and updates the portfolio.

        :param asset: The name of the asset.
        :param quantity: The quantity of the asset to sell.
        :param price: The price per unit of the asset.
        :raises ValueError: If the quantity or price is negative.
        :raises ValueError: If the asset is not in the portfolio or quantity exceeds holdings.
        """
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive.")
        if asset not in self.assets or self.assets[asset] < quantity:
            raise ValueError("Insufficient quantity of the asset to sell.")
        total_revenue = quantity * price
        self.cash += total_revenue
        self.assets[asset] -= quantity
        if self.assets[asset] == 0:
            del self.assets[asset]

    def calculate_value(self) -> float:
        """
        Calculates the total value of the portfolio.

        :return: The total value of the portfolio (cash + asset values).
        """
        total_value = self.cash
        for asset, quantity in self.assets.items():
            # Assuming a placeholder price of 1.0 for simplicity
            total_value += quantity * 1.0
        return total_value


# Example usage
if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.add_cash(1000)
    portfolio.buy_asset("AAPL", 5, 150)
    portfolio.sell_asset("AAPL", 2, 160)
    print(f"Portfolio value: {portfolio.calculate_value()}")
