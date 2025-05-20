from vibebacktest.vibebacktest.portfolio import Portfolio
import openbb

class Backtester:
    def __init__(self, strategy):
        self.strategy = strategy
        self.portfolio = Portfolio()
        self.holdings_history = []
        self.portfolio_value_history = []

    def run_monthly_backtest(self):
        """Execute the monthly backtesting workflow."""
        # Step 1: Screener
        screened_assets = self._run_screener()
        
        # Step 2: Transactions
        self._execute_transactions(screened_assets)
        
        # Step 3: Calculations
        portfolio_value = self._calculate_portfolio_value()
        invested_capital = self.portfolio.get_invested_capital()
        
        # Store intermediate results
        self.holdings_history.append(self.portfolio.get_holdings())
        self.portfolio_value_history.append(portfolio_value)
        
        return {
            "portfolio_value": portfolio_value,
            "invested_capital": invested_capital,
            "holdings": self.portfolio.get_holdings()
        }

    def _run_screener(self):
        """Use openbb to filter assets based on strategy criteria."""
        # Example: Fetch market data and apply strategy filters
        market_data = openbb.equity.price.historical(symbol="SPY", start_date="2023-01-01")
        filtered_assets = self.strategy.filter_assets(market_data)
        return filtered_assets

    def _execute_transactions(self, screened_assets):
        """Rebalance portfolio based on screening results."""
        current_holdings = self.portfolio.get_holdings()
        
        # Example: Buy new assets and sell underperforming ones
        for asset, quantity in screened_assets.items():
            if asset not in current_holdings:
                self.portfolio.buy_asset(asset, quantity)
            else:
                self.portfolio.rebalance_asset(asset, quantity)
        
        # Remove assets not in the new screening
        for asset in current_holdings:
            if asset not in screened_assets:
                self.portfolio.sell_asset(asset)

    def _calculate_portfolio_value(self):
        """Calculate current portfolio value using openbb."""
        total_value = 0
        for asset, quantity in self.portfolio.get_holdings().items():
            price = openbb.equity.price.current(asset)
            total_value += price * quantity
        return total_value
