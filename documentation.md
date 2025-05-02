# VibeBackTest - Developer Documentation

## 1. Detailed Description of Application

**VibeBackTest** is a command-line interface (CLI) application built in Python. Its primary purpose is to backtest investment strategies based on historical market data. Users define their investment strategy in a YAML configuration file, specifying parameters like starting capital, monthly additions, asset screening criteria, and portfolio rebalancing rules.

The application takes this strategy file, along with a start and end date (Year/Month format), as input. It then simulates the execution of this strategy over the specified period, month by month.

**Core Workflow:**

1.  **Validation:** Before starting the backtest, the application validates the inputs:
    *   Ensures the start date is chronologically before the end date.
    *   Checks if the backtest duration is at least one full year.
    *   Verifies that the specified strategy YAML file exists and is well-formed according to the expected structure.
2.  **Monthly Backtesting Loop:** The application iterates month by month from the start date to the end date. In each monthly cycle, it performs the following steps:
    *   **Screener:** Uses the criteria defined in the strategy YAML to screen for assets (e.g., stocks, ETFs) using data retrieved via the `openbb` library. It selects a predefined number of top-ranking assets based on the strategy.
    *   **Transactions:** Simulates portfolio adjustments based on the screener results and rebalancing rules:
        *   Identifies assets currently held in the portfolio but *not* selected by the screener for the current month – these are marked for selling.
        *   Identifies assets selected by the screener but *not* currently in the portfolio – these are marked for buying.
        *   Calculates buy/sell orders based on the rebalancing rules (e.g., allocate capital equally among selected assets).
        *   Simulates the execution of these buy/sell transactions.
    *   **Calculation:** After transactions, it calculates:
        *   The total current market value of the portfolio based on the prices of held assets at the end of the month.
        *   The total amount of money invested so far (initial capital + all monthly additions up to that point).
    *   **Storing:** Records the state for the current month:
        *   List of assets held in the portfolio and their quantities.
        *   Details of buy/sell transactions executed.
        *   Calculated portfolio value.
        *   Total invested amount.
        *(Note: For this initial version, storing might happen in memory during the run, with only the final results being displayed. More persistent storage could be added later).*
3.  **Results Presentation:** Once the loop completes (reaches the end date), the application displays a summary of the backtest results:
    *   The assets held in the portfolio in the final month.
    *   The final calculated portfolio value.
    *   The total amount of money invested over the entire period.

The application relies heavily on the `openbb` library for accessing historical financial data, screening assets, and potentially fetching price information needed for calculations and transaction simulation.

## 2. List of Steps to Accomplish the Target (Build the App)

Here’s a suggested sequence of steps for developing the `VibeBackTest` application:

1.  **Setup Project Environment:**
    *   Create a project directory (e.g., `vibebacktest`).
    *   Set up a Python virtual environment (e.g., `python -m venv venv`).
    *   Activate the virtual environment (`source venv/bin/activate` on Linux/macOS or `.\venv\Scripts\activate` on Windows).
    *   Install necessary libraries: `pip install openbb pyyaml python-dateutil` (We'll use `python-dateutil` for easier month increments). Create a `requirements.txt` file.

2.  **Implement Command-Line Argument Parsing:**
    *   Use the `argparse` module (standard library).
    *   Define arguments for:
        *   `--strategy` (path to the strategy YAML file, required).
        *   `--start-date` (start date in 'YYYY-MM' format, required).
        *   `--end-date` (end date in 'YYYY-MM' format, required).

3.  **Implement Strategy Loading and Validation (Phase 1):**
    *   Create functions or a class to handle the strategy file.
    *   Use `PyYAML` to load the YAML file specified by the `--strategy` argument.
    *   Implement validation logic:
        *   Check if the file exists.
        *   Use `try...except` block during YAML parsing to catch formatting errors.
        *   Validate the presence and basic types of required keys (e.g., `initial_capital`, `monthly_addition`, `rebalancing`, `screener`).
        *   Parse `--start-date` and `--end-date` into `datetime` objects.
        *   Validate the date logic (start < end, period >= 1 year). Handle potential `ValueError` during date parsing.

4.  **Design and Implement Data Structures:**
    *   Decide how to represent the portfolio (e.g., a dictionary like `{'AAPL': {'quantity': 10}, 'MSFT': {'quantity': 5}}`).
    *   Decide how to store cash available.
    *   Decide how to store historical data collected during the backtest (e.g., a list of dictionaries, where each dictionary represents a month's state).

5.  **Implement Core Backtesting Logic (Phase 2):**
    *   Create the main backtesting loop that iterates month by month from the start date to the end date. Use `dateutil.relativedelta.relativedelta(months=1)` for easy increments.
    *   **Inside the loop:**
        *   **a. Screener:**
            *   Call `openbb` functions (e.g., `openbb.economy.screener` or similar, you'll need to explore the specific `openbb` functions that match your criteria).
            *   Filter/rank the results based on the `screener` criteria from the YAML.
            *   Select the top `max_assets` as defined in the `rebalancing` section of the YAML.
        *   **b. Transactions:**
            *   Determine which assets to sell (in portfolio but not in current screener list).
            *   Determine which assets to buy (in screener list but not in portfolio, or needing adjustment based on rebalancing).
            *   Implement the rebalancing logic (e.g., calculate target value per asset based on current portfolio value and `max_assets` for equal weighting).
            *   Simulate buys/sells: Adjust asset quantities in the portfolio data structure and update the available cash. You will likely need to fetch asset prices using `openbb` for the relevant date to perform these calculations.
        *   **c. Calculation:**
            *   Fetch end-of-month prices for all assets held in the portfolio using `openbb`.
            *   Calculate the total market value of the portfolio (sum of `quantity * price` for all assets) plus any remaining cash.
            *   Keep track of the total invested capital (initial + cumulative monthly additions).
        *   **d. Storing:**
            *   Append the relevant data for the current month (portfolio holdings, transactions list, portfolio value, invested capital) to your historical data structure.

6.  **Implement Results Presentation (Phase 3):**
    *   After the loop finishes, access the last entry in your historical data structure.
    *   Print the final portfolio holdings, the final portfolio value, and the total invested capital in a clear, readable format.

7.  **Add Error Handling and Logging:**
    *   Wrap `openbb` calls in `try...except` blocks to handle potential API errors or data availability issues.
    *   Add basic logging (`logging` module) to show progress (e.g., "Processing Month YYYY-MM...") and report errors.

8.  **Refine and Document Code:**
    *   Add comments and docstrings to your Python code.
    *   Refactor code for clarity and efficiency.
    *   Ensure the command-line interface is user-friendly.

## 3. Technologies and Libraries to be Used

*   **Language:** Python (Version 3.8 or higher recommended)
*   **Core Library:**
    *   `openbb`: For accessing financial market data, screening assets, and fetching historical prices. (Note: You might interact with its SDK components rather than the terminal itself).
*   **Configuration:**
    *   `PyYAML`: For parsing the strategy configuration files (`.yaml`).
*   **Date/Time Handling:**
    *   `datetime` (Python standard library): For basic date objects.
    *   `python-dateutil`: For easier date calculations, especially adding months (`relativedelta`).
*   **Command-Line Interface:**
    *   `argparse` (Python standard library): For parsing command-line arguments.
*   **Environment Management:**
    *   `venv` (Python standard library): Recommended for creating isolated Python environments.

## 4. Files to be Created

Here is a suggested file structure for the project. You can adapt this as the project grows.

```
vibebacktest/
│
├── venv/                     # Python virtual environment (created by `python -m venv venv`)
│
├── strategies/               # Directory to store strategy YAML files
│   └── example_strategy.yaml # Example strategy configuration
│
├── vibebacktest/             # Source code directory (could also be named `src`)
│   ├── __init__.py           # Makes the directory a Python package
│   ├── main.py               # Main script entry point, handles CLI args, orchestrates workflow
│   ├── strategy.py           # Functions/class for loading and validating strategy YAML
│   ├── backtester.py         # Core backtesting loop logic, screener, transactions, calculations
│   ├── portfolio.py          # Class/functions to manage portfolio state (holdings, cash)
│   ├── data_provider.py      # (Optional but recommended) Wraps openbb calls for fetching data/screening
│   └── utils.py              # Utility functions (e.g., date formatting, calculations)
│
├── requirements.txt          # Lists project dependencies (openbb-terminal, PyYAML, python-dateutil)
└── README.md                 # Project documentation (this file)
```

**File Descriptions:**

*   `strategies/example_strategy.yaml`: An example YAML file defining an investment strategy (see design below).
*   `vibebacktest/main.py`: The main executable script. Parses arguments (`argparse`), loads the strategy (`strategy.py`), initializes the portfolio (`portfolio.py`), runs the backtest loop (`backtester.py`), and presents the final results.
*   `vibebacktest/strategy.py`: Contains code to read the `.yaml` file using `PyYAML`, validate its structure and content, and make the strategy parameters easily accessible to the rest of the application.
*   `vibebacktest/backtester.py`: Holds the primary logic. Contains the monthly loop. It will call the screener function, the transaction simulation logic, and the portfolio calculation logic. It likely interacts with `portfolio.py` and `data_provider.py`.
*   `vibebacktest/portfolio.py`: Manages the state of the simulated portfolio. Includes functions or methods to add/remove assets, update quantities, manage cash, and calculate total invested capital.
*   `vibebacktest/data_provider.py`: (Optional) Abstract interface for getting data from `openbb`. This makes it easier to test other parts of the application without making live API calls and isolates the `openbb` dependency. Functions like `get_price(ticker, date)`, `screen_assets(criteria)` could go here.
*   `vibebacktest/utils.py`: Contains small, reusable helper functions used across different modules (e.g., date manipulation, financial calculations if needed).
*   `requirements.txt`: File listing dependencies for `pip install -r requirements.txt`. Content would be like:
    ```
    openbb-terminal
    PyYAML
    python-dateutil
    ```
*   `README.md`: This documentation file.

---

## Strategy YAML File Design and Example

The strategy configuration file drives the backtesting process. Here's a proposed structure:

```yaml
# --- VibeBackTest Strategy Configuration ---

# Initial amount of cash to start the backtest with.
initial_capital: 10000.00

# Amount of new cash added to the portfolio at the beginning of each month.
# Set to 0 if no new money is added regularly.
monthly_addition: 500.00

# --- Rebalancing Rules ---
rebalancing:
  # How often to run the screener and rebalance the portfolio.
  # For now, only "monthly" is supported due to the core loop structure.
  frequency: monthly

  # How to allocate capital among the selected assets.
  # "equal": Divide capital equally among the selected assets.
  # Future options could include "market_cap", "custom_weights", etc.
  weighting: equal

  # The target number of assets to hold after rebalancing.
  # The screener will find potentially many assets, but the portfolio
  # will be adjusted to hold only this number of top-ranked ones.
  max_assets: 10

# --- Asset Screener Configuration ---
# Defines the criteria used to select assets each month.
# This needs to map closely to the capabilities of the openbb screener function.
screener:
  # Type of asset to screen for (e.g., 'equity', 'etf', 'crypto')
  # This should align with openbb preset/filter options.
  asset_type: equity

  # Define screening criteria. This is an example structure.
  # The exact 'metric' names must match what openbb's screener expects.
  # Explore openbb documentation for available screening metrics.
  criteria:
    # Example 1: Market Capitalization between $2B and $200B
    - metric: MarketCap
      min: 2000000000 # $2 Billion
      max: 200000000000 # $200 Billion
    # Example 2: Price-to-Earnings (P/E) ratio below 25
    - metric: P/E
      min: 0 # Optional: minimum P/E (e.g., must be positive)
      max: 25
    # Example 3: Average Daily Volume over 1 million shares
    - metric: AverageVolume
      min: 1000000

  # How to rank the assets that pass the criteria filters.
  # The 'metric' must be a value available from the screener results.
  # 'order' can be 'descending' (highest value first) or 'ascending' (lowest value first).
  ranking:
    metric: MarketCap # Rank by Market Cap after filtering
    order: descending # Pick the ones with the highest market cap


**Example Usage (How a user would run the app):**

```bash
python vibebacktest/main.py --strategy strategies/example_strategy.yaml --start-date 2020-01 --end-date 2023-12
```

---
This documentation provides a solid foundation. Remember to explore the specific functions within the `openbb` library that you'll need for screening and data retrieval, as the exact parameters and available metrics in the `screener` section will depend on that.

If any part is unclear or you need more details on a specific step (like the exact `openbb` functions or more complex rebalancing logic), please ask!
