import argparse
import re
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def validate_date_format(date_str):
    """Validate date format as YYYY-MM."""
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Validating date format for input: %s", date_str)
    if not re.match(r"^\d{4}-\d{2}$", date_str):
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_str}. Expected format: YYYY-MM.")
    return date_str

def parse_arguments():
    """Parse and validate command-line arguments."""
    parser = argparse.ArgumentParser(description="VibeBackTest CLI")
    parser.add_argument("--strategy", required=True, help="Path to the YAML configuration file defining the investment strategy.")
    parser.add_argument("--start-date", required=True, type=validate_date_format, help="Start date in YYYY-MM format.")
    parser.add_argument("--end-date", required=True, type=validate_date_format, help="End date in YYYY-MM format.")
    
    return parser.parse_args()

import logging
from strategy import load_strategy
from backtester import run_backtest
from portfolio import Portfolio
from data_provider import DataProvider

def main():
    """Main entry point for the CLI."""
    logging.basicConfig(level=logging.INFO)
    try:
        args = parse_arguments()
        logging.info("Parsed arguments: %s", args)

        # Load strategy
        strategy = load_strategy(args.strategy)
        logging.info("Loaded strategy: %s", strategy)

        # Initialize DataProvider and Portfolio
        data_provider = DataProvider()
        portfolio = Portfolio()

        # Run backtest
        results = run_backtest(strategy, args.start_date + "-01", args.end_date + "-01")
        if "error" in results:
            raise RuntimeError(results["error"])

        # Display final results
        final_month = results["results"][-1]
        logging.info("Final Portfolio Value: %.2f", final_month["portfolio_value"])
        logging.info("Total Invested Capital: %.2f", final_month["total_invested"])
        logging.info("Final Holdings: %s", portfolio.assets)

    except Exception as e:
        logging.error("Error: %s", e, exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
