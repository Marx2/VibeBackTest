## Recent Changes

- Completed the initial implementation of the VibeBackTest application.
- Updated `progress.md` to reflect completed tasks and next steps.

## Current Focus

- Implementing screener logic and integrating with the `openbb` library.
- Adding transaction simulation and portfolio rebalancing logic.
- Developing unit tests for all modules using `pytest`.

## Open Questions/Issues

- None at the moment.
[2025-05-20 20:22:50] - Updated the project with an example YAML file for strategy configuration (`strategy_example.yaml`), implemented loading and validation logic in `strategy.py`, and tested the functionality in `backtester.py`. The test confirmed successful loading and validation of the strategy.
### [2025-05-20 20:25:18] - Screener Functionality Plan

#### Objective:
Develop a stock screener leveraging the OpenBB library to filter stocks based on conditions defined in the strategy.

#### High-Level Design:
1. **Integration with OpenBB Library**:
   - Use OpenBB's stock screening capabilities to fetch and filter stock data.
   - Ensure compatibility with the conditions defined in the strategy YAML file (`strategy_example.yaml`).

2. **Workflow**:
   - **Input**: Conditions from the strategy file.
   - **Processing**: Use OpenBB to screen stocks based on the conditions.
   - **Output**: A filtered list of stocks to be used by the backtester or portfolio manager.

3. **Components**:
   - **Strategy Parser**: Extract conditions from `strategy_example.yaml`.
   - **Screener Module**: Interface with OpenBB to apply the conditions and fetch results.
   - **Integration with Backtester**: Pass the filtered stocks to `backtester.py` for further analysis.

#### Implementation Steps:
1. **Update `requirements.txt`**:
   - Add OpenBB library dependency.

2. **Create Screener Module**:
   - File: `vibebacktest/screener.py`
   - Responsibilities:
     - Parse conditions from the strategy.
     - Use OpenBB to fetch stock data.
     - Apply filtering logic.

3. **Modify `strategy.py`**:
   - Add functionality to extract and validate conditions for the screener.

4. **Integrate with Backtester**:
   - Update `backtester.py` to accept the filtered stock list from the screener.

5. **Testing**:
   - Write unit tests for the screener module.
   - Validate integration with the strategy and backtester.

#### Next Steps:
1. Confirm the specific conditions to be used for screening.
2. Implement the screener module (`screener.py`).
3. Update the Memory Bank with progress and decisions.