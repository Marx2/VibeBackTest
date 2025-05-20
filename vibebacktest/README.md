# VibeBackTest

VibeBackTest is a Python-based command-line interface (CLI) application designed to backtest investment strategies using historical market data. Users define their strategies in YAML configuration files, and the application simulates the execution of these strategies over a specified time period.

---

## Features

- **Command-Line Interface:** Accepts user inputs for strategy configuration and backtesting period.
- **Strategy Configuration:** Define investment strategies in YAML files.
- **Backtesting Logic:** Simulates monthly portfolio adjustments based on strategy rules.
- **Results Presentation:** Displays portfolio value, invested capital, and final holdings.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd vibebacktest
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the application with the following arguments:
```bash
python vibebacktest/main.py --strategy <path-to-strategy.yaml> --start-date YYYY-MM --end-date YYYY-MM
```

---

## Project Structure

```
vibebacktest/
├── strategies/               # Directory to store strategy YAML files
├── vibebacktest/             # Source code directory
│   ├── __init__.py           # Makes the directory a Python package
│   ├── main.py               # Main script entry point
│   ├── strategy.py           # Strategy YAML handling
│   ├── backtester.py         # Core backtesting logic
│   ├── portfolio.py          # Portfolio management
│   ├── data_provider.py      # Data fetching and abstraction
│   └── utils.py              # Utility functions
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## License

This project is licensed under the MIT License.