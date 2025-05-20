class Portfolio:
    """
    A class to manage the portfolio state during the backtest.
    """

    def __init__(self, initial_cash):
        """
        Initialize the portfolio with cash and empty holdings.

        Args:
            initial_cash (float): Initial amount of cash in the portfolio.
        """
        self.cash = initial_cash
        self.holdings = {}

    def add_cash(self, amount):
        """
        Add cash to the portfolio.

        Args:
            amount (float): Amount of cash to add.
        """
        self.cash += amount

    def buy_asset(self, symbol, quantity, price):
        """
        Buy an asset and update the portfolio.

        Args:
            symbol (str): Asset symbol.
            quantity (int): Quantity to buy.
            price (float): Price per unit of the asset.
        """
        total_cost = quantity * price
        if total_cost > self.cash:
            raise ValueError("Insufficient cash to buy asset.")
        self.cash -= total_cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity

    def sell_asset(self, symbol, quantity, price):
        """
        Sell an asset and update the portfolio.

        Args:
            symbol (str): Asset symbol.
            quantity (int): Quantity to sell.
            price (float): Price per unit of the asset.
        """
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Insufficient holdings to sell asset.")
        total_revenue = quantity * price
        self.cash += total_revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]

    def calculate_portfolio_value(self, prices):
        """
        Calculate the total value of the portfolio.

        Args:
            prices (dict): Dictionary of asset prices (symbol -> price).

        Returns:
            float: Total portfolio value (cash + holdings value).
        """
        holdings_value = sum(
            quantity * prices.get(symbol, 0) for symbol, quantity in self.holdings.items()
        )
        return self.cash + holdings_value