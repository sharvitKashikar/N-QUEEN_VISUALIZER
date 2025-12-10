# N-Queen Solver Logic and Visualization

This document describes the core logic behind solving the N-Queen problem within the visualizer, specifically focusing on the `solveNQUtil` function introduced in `N-queen.py`.

## The `solveNQUtil` Function

`solveNQUtil` implements a backtracking algorithm to find a solution for placing N queens on an NxN chessboard such that no two queens attack each other. It includes direct calls to visualization functions to show the search process step-by-step.

### Parameters

- `draw`: A function (likely from a UI/Grid component) that refreshes the visual representation of the board after a change. This is crucial for real-time visualization of the backtracking process.
- `grid`: A 2D array representing the chessboard. Each element in the grid is expected to be an object (e.g., a `Spot` or `Cell` object) that can respond to `make_barrier()` and `make_reset()` calls.
- `col`: The current column being considered for placing a queen. The function attempts to place a queen in this column.

### Algorithm Overview

1.  **Base Case**: If all queens have been successfully placed (i.e., `col` reaches `ROW`, where `ROW` is the board size), a solution is found, and the function returns `True`.
2.  **Iterate Rows**: For the current `col`, the function iterates through each `row` from `0` to `ROW-1`.
3.  **Safety Check**: For each `(row, col)` position, it calls `isSafe(draw, grid, row, col)` to determine if a queen can be safely placed there without being attacked by any previously placed queens.
4.  **Placement and Recurse**: 
    *   If safe, the queen is 'placed' visually by calling `grid[row][col].make_barrier()` (marking the cell as occupied) and immediately calling `draw()` to update the display.
    *   The function then recursively calls `solveNQUtil(draw, grid, col + 1)` to place the next queen in the subsequent column.
5.  **Backtrack**: 
    *   If the recursive call returns `False` (meaning placing a queen in `(row, col)` did not lead to a solution), the function 'removes' the queen from `(row, col)`.
    *   This is done visually by calling `grid[row][col].make_reset()` and `draw()` to clear the cell on the board.
6.  **Return**: If a solution is found at any point in the recursion, `True` is returned. If no safe placement is found for the current `col` after trying all rows, `False` is returned, triggering backtracking in the previous call.