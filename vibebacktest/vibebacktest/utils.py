import re
from datetime import datetime, timedelta

def validate_date_format(date_str):
    """Validates if a date string is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def increment_month(date_str):
    """Increments a given date by one month."""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    year = date.year
    month = date.month + 1
    if month > 12:
        year += 1
        month = 1
    try:
        return datetime(year, month, date.day).strftime('%Y-%m-%d')
    except ValueError:
        # Handle end-of-month edge cases (e.g., 2025-01-31 → 2025-02-28)
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)
        last_day = next_month - timedelta(days=1)
        return last_day.strftime('%Y-%m-%d')

def log_message(message, verbose):
    """Logs messages conditionally based on verbosity."""
    if verbose:
        print(message)
