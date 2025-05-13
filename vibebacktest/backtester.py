import datetime
from typing import Dict, List

def run_backtest(strategy: Dict, start_date: str, end_date: str) -> Dict:
    """
    Runs a backtest for the given strategy over the specified date range.

    Args:
        strategy (dict): A dictionary defining the strategy logic.
        start_date (str): The start date of the backtest in 'YYYY-MM-DD' format.
        end_date (str): The end date of the backtest in 'YYYY-MM-DD' format.

    Returns:
        dict: A dictionary containing the portfolio state and transactions for each month.
    """
    try:
        # Parse dates
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        if start > end:
            raise ValueError("Start date must be before end date.")

        # Initialize portfolio and results
        portfolio_value = 100000  # Starting portfolio value
        total_invested = 0
        monthly_results = []

        # Iterate through each month
        current_date = start
        while current_date <= end:
            # Placeholder: Screen assets using strategy
            screened_assets = strategy.get("assets", [])

            # Placeholder: Simulate buy/sell transactions
            transactions = [{"asset": asset, "action": "buy", "amount": 1000} for asset in screened_assets]

            # Update portfolio value and total invested
            portfolio_value += sum(txn["amount"] for txn in transactions)
            total_invested += sum(txn["amount"] for txn in transactions)

            # Store monthly results
            monthly_results.append({
                "date": current_date.strftime("%Y-%m"),
                "portfolio_value": portfolio_value,
                "total_invested": total_invested,
                "transactions": transactions
            })

            # Move to the next month
            next_month = current_date.month % 12 + 1
            next_year = current_date.year + (current_date.month // 12)
            current_date = current_date.replace(year=next_year, month=next_month, day=1)

        return {"results": monthly_results}

    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    sample_strategy = {"assets": ["AAPL", "GOOG", "MSFT"]}
    backtest_results = run_backtest(sample_strategy, "2023-01-01", "2023-12-31")
    print(backtest_results)
