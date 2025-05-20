# System Patterns

This file documents recurring patterns and standards used in the project.

---

## Coding Patterns

- Modular design with dedicated Python modules for CLI, strategy handling, backtesting logic, portfolio management, and data fetching.
- Use of `argparse` for command-line argument parsing.
- YAML-based configuration for strategy definitions.

## Architectural Patterns

- Separation of concerns: Each module handles a specific aspect of the application (e.g., `strategy.py` for YAML parsing, `portfolio.py` for portfolio management).
- Integration with external libraries (`openbb`) through an abstraction layer (`data_provider.py`).

## Testing Patterns

- Unit testing with `pytest`.
- Mocking external dependencies (`openbb`) using `pytest-mock`.
- Coverage measurement with `pytest-cov`.

---

*Log of updates will be appended as footnotes to the end of this file.*