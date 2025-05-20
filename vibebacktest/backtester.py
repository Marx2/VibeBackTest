from datetime import datetime
from dateutil.relativedelta import relativedelta

def run_backtest(strategy, start_date, end_date):
    """
    Run the backtesting simulation.

    Args:
        strategy (dict): Parsed strategy configuration.
        start_date (str): Start date in YYYY-MM format.
        end_date (str): End date in YYYY-MM format.

    Returns:
        None
    """
    # Parse dates
    start = datetime.strptime(start_date, "%Y-%m")
    end = datetime.strptime(end_date, "%Y-%m")

    if start >= end:
        raise ValueError("Start date must be earlier than end date.")
    if (end - start).days < 365:
        raise ValueError("Backtest duration must be at least one year.")

    print(f"Starting backtest from {start_date} to {end_date}...")

    # Initialize portfolio
    portfolio = {
        "cash": strategy["initial_capital"],
        "holdings": {},
        "history": []
    }

    # Monthly loop
    current_date = start
    while current_date <= end:
        print(f"Processing month: {current_date.strftime('%Y-%m')}")

        # Placeholder for screener, transactions, and calculations
        # Screener logic would go here
        # Transaction simulation would go here
        # Portfolio value calculation would go here

        # Advance to the next month
        current_date += relativedelta(months=1)

    print("Backtest complete.")
from strategy import load_strategy

def test_strategy_loading():
    """
    Test the loading and validation of a strategy YAML file.
    """
    try:
        strategy = load_strategy("vibebacktest/strategy_example.yaml")
        print("Strategy loaded successfully:")
        print(strategy)
    except Exception as e:
        print(f"Error loading strategy: {e}")

if __name__ == "__main__":
    test_strategy_loading()