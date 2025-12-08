def solveMaze(maze):
    n = len(maze)
    sol = []
    path = ""

    # Directions: (move, row change, col change)
    dirs = [('D', 1, 0), ('R', 0, 1)]

    def backtrack(r, c, path):
        # If reached destination
        if r == n - 1 and c == n - 1:
            sol.append(path)
            return

        for move, dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            # Check boundaries
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1:
                # Mark current cell as visited
                maze[nr][nc] = -1
                backtrack(nr, nc, path + move)
                # Unmark (backtrack)
                maze[nr][nc] = 1

    # Start only if starting point is free
    if maze[0][0] == 1:
        maze[0][0] = -1   # mark start visited
        backtrack(0, 0, "")

    return sol


# Example Input
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

# Print solutions
paths = solveMaze(maze)
print("All possible paths:", paths)
