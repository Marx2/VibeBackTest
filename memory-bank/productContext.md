# Product Context

This file provides a high-level overview of the project and the expected product that will be created. Initially, it is based upon projectBrief.md (if provided) and all other available project-related information in the working directory. This file is intended to be updated as the project evolves and should be used to inform all other modes of the project's goals and context.

---

## Project Goal

Develop the **VibeBackTest** application, a Python-based CLI tool for backtesting investment strategies using historical market data.

## Key Features

- Command-line interface for user inputs.
- Strategy configuration via YAML files.
- Monthly backtesting loop with asset screening, transactions, and portfolio rebalancing.
- Results presentation including portfolio value and invested capital.

## Overall Architecture

- Modular Python codebase with dedicated modules for CLI, strategy handling, backtesting logic, portfolio management, and data fetching.
- Integration with the `openbb` library for financial data access.
- Testing framework using `pytest` with mocked dependencies for reliability.

---

*Log of updates will be appended as footnotes to the end of this file.*