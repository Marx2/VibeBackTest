import argparse
from datetime import datetime

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_str}. Use YYYY-MM-DD.")

parser = argparse.ArgumentParser(description='VibeBackTest CLI')
parser.add_argument('--strategy', required=True, help='Path to strategy YAML file')
parser.add_argument('--start-date', required=True, type=validate_date, help='Start date (YYYY-MM-DD)')
parser.add_argument('--end-date', required=True, type=validate_date, help='End date (YYYY-MM-DD)')
parser.add_argument('--verbose', action='store_true', default=False, help='Enable verbose output')

args = parser.parse_args()

print("Parsed arguments:")
print(f"Strategy: {args.strategy}")
print(f"Start Date: {args.start_date}")
print(f"End Date: {args.end_date}")
print(f"Verbose: {args.verbose}")
