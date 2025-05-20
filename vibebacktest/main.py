import argparse
from vibebacktest.strategy import load_strategy
from vibebacktest.backtester import run_backtest

def main():
    parser = argparse.ArgumentParser(description="VibeBackTest CLI Application")
    parser.add_argument("--strategy", required=True, help="Path to the strategy YAML file")
    parser.add_argument("--start-date", required=True, help="Start date in YYYY-MM format")
    parser.add_argument("--end-date", required=True, help="End date in YYYY-MM format")
    args = parser.parse_args()

    # Load and validate strategy
    strategy = load_strategy(args.strategy)

    # Run backtest
    run_backtest(strategy, args.start_date, args.end_date)

if __name__ == "__main__":
    main()