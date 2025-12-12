# N-Queen Visualizer

This repository contains a Python-based N-Queen problem solver with a Pygame visualizer.

## Features

- Solves the N-Queen problem for a user-defined board size (N).
- Visualizes the placement of queens on an N x N chessboard using Pygame.
- Allows navigation through different solutions (if multiple exist) for a given N.

## Setup

To run the visualizer, you need to have Python and Pygame installed.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/sharvitKashikar/N-QUEEN_VISUALIZER.git
    cd N-QUEEN_VISUALIZER
    ```

2.  **Install Pygame:**

    If you don't have Pygame installed, you can install it using pip:

    ```bash
    pip install pygame
    ```

## Usage

To start the N-Queen visualizer, run the `game.py` script:

```bash
python game.py
```

--- 

### Running the Application:

1.  **Input N:** When prompted in the console, enter the desired size 'N' for the N x N chessboard (e.g., `4` for a 4x4 board).
2.  **Visualizer Window:** A Pygame window will open, displaying the N-Queen solutions.
3.  **Navigation:**
    *   Use the **left arrow key** to view the previous solution.
    *   Use the **right arrow key** to view the next solution.
    *   Press the **'R' key** to restart and enter a new 'N'.
    *   Close the window to exit the application.
