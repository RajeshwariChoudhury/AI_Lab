import heapq

# The goal state of the 8-puzzle
GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Possible moves for the empty space (0)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right


class PuzzleState:
    def __init__(self, board, moves=0, parent=None):
        self.board = board
        self.moves = moves
        self.parent = parent
        self.empty_pos = self.find_empty_pos()

    def find_empty_pos(self):
        """Find the position of the empty tile (0) in the board."""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def get_neighbors(self):
        """Generate all valid neighbors (next states) from the current state."""
        neighbors = []
        empty_row, empty_col = self.empty_pos
        for move in MOVES:
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Create a new state by swapping the empty space with the adjacent tile
                new_board = [list(row) for row in self.board]
                new_board[empty_row][empty_col], new_board[new_row][new_col] = new_board[new_row][new_col], \
                new_board[empty_row][empty_col]
                neighbors.append(PuzzleState(tuple(tuple(row) for row in new_board), self.moves + 1, self))
        return neighbors

    def is_goal(self):
        """Check if the current state matches the goal state."""
        return self.board == GOAL_STATE

    def manhattan_distance(self):
        """Heuristic: Sum of Manhattan distances of tiles from the goal position."""
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = self.board[i][j]
                if tile != 0:
                    goal_row, goal_col = divmod(tile - 1, 3)
                    distance += abs(goal_row - i) + abs(goal_col - j)
        return distance

    def __lt__(self, other):
        """For comparison in priority queue (based on f = g + h)."""
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())


def a_star(start_state):
    """Implement A* search algorithm to solve the 8-puzzle."""
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, start_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            # Reconstruct the path from start to goal
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1]  # Return reversed path

        closed_set.add(current_state.board)

        # Explore neighbors
        for neighbor in current_state.get_neighbors():
            if neighbor.board not in closed_set:
                heapq.heappush(open_list, neighbor)

    return None  # No solution found


def print_solution(path):
    """Print the solution path."""
    for step in path:
        for row in step:
            print(row)
        print()


def main():
    # Example initial state
    initial_state = PuzzleState((
        (1, 2, 3),
        (4, 5, 6),
        (0, 7, 8)
    ))

    # Solve the puzzle using A* search
    solution = a_star(initial_state)

    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
