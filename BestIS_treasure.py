import heapq

# Directions for grid movement (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def manhattan_distance(x, y, tx, ty):
    """Calculate the Manhattan distance between (x, y) and the treasure location (tx, ty)."""
    return abs(x - tx) + abs(y - ty)


def best_first_search(grid, start, treasure):
    """Perform Best-First Search to find the treasure in the grid."""
    rows, cols = len(grid), len(grid[0])
    tx, ty = treasure  # Treasure location
    sx, sy = start  # Starting location

    # Priority queue stores tuples (heuristic_value, x, y)
    pq = []
    heapq.heappush(pq, (manhattan_distance(sx, sy, tx, ty), sx, sy))

    # Set to track visited cells
    visited = set()
    visited.add((sx, sy))

    while pq:
        # Get the current cell with the lowest heuristic value
        heuristic, x, y = heapq.heappop(pq)

        # Check if we've reached the treasure
        if (x, y) == (tx, ty):
            print(f"Treasure found at ({x}, {y})!")
            return True

        # Explore neighbors
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            # Check if the neighbor is within bounds and not visited
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                visited.add((nx, ny))

                # Push the neighbor into the priority queue with its heuristic value
                heapq.heappush(pq, (manhattan_distance(nx, ny, tx, ty), nx, ny))

    print("Treasure not found!")
    return False


def main():
    # Take grid dimensions from the user
    rows = int(input("Enter the number of rows in the grid: "))
    cols = int(input("Enter the number of columns in the grid: "))

    # Take the positions for start and treasure from the user
    start_x = int(input(f"Enter the start point's x coordinate (0 to {rows - 1}): "))
    start_y = int(input(f"Enter the start point's y coordinate (0 to {cols - 1}): "))
    treasure_x = int(input(f"Enter the treasure's x coordinate (0 to {rows - 1}): "))
    treasure_y = int(input(f"Enter the treasure's y coordinate (0 to {cols - 1}): "))

    # Ensure valid input (start point and treasure are within bounds)
    if not (0 <= start_x < rows and 0 <= start_y < cols and 0 <= treasure_x < rows and 0 <= treasure_y < cols):
        print("Invalid coordinates. Please make sure the coordinates are within the grid size.")
        return

    start = (start_x, start_y)
    treasure = (treasure_x, treasure_y)

    # Create the grid (each cell will contain its Manhattan distance from the treasure)
    grid = [[manhattan_distance(i, j, treasure_x, treasure_y) for j in range(cols)] for i in range(rows)]

    # Perform Best-First Search to find the treasure
    print("Starting Best-First Search...")
    best_first_search(grid, start, treasure)


if __name__ == "__main__":
    main()
