import math
import heapq
import tkinter as tk
import time


# Define the Cell class
class Cell:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0


# Define grid size
ROW = 9
COL = 10
CELL_SIZE = 50


def is_valid(row, col):
    return 0 <= row < ROW and 0 <= col < COL


def is_unblocked(grid, row, col):
    return grid[row][col] == 1


def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]


def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5


def trace_path(canvas, cell_details, dest):
    path = []
    row, col = dest

    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        row, col = cell_details[row][col].parent_i, cell_details[row][col].parent_j
    path.append((row, col))
    path.reverse()

    for (r, c) in path:
        canvas.create_rectangle(c * CELL_SIZE, r * CELL_SIZE, (c + 1) * CELL_SIZE, (r + 1) * CELL_SIZE, fill="blue")
        canvas.update()
        time.sleep(0.2)


def a_star_search(canvas, grid, src, dest):
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or the destination is blocked")
        return

    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    i, j = src
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    open_list = []
    heapq.heappush(open_list, (0.0, i, j))
    found_dest = False

    while open_list:
        p = heapq.heappop(open_list)
        i, j = p[1], p[2]
        closed_list[i][j] = True

        canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE, (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE, fill="yellow")
        canvas.update()
        time.sleep(0.05)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i, new_j = i + dir[0], j + dir[1]

            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                if is_destination(new_i, new_j, dest):
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    trace_path(canvas, cell_details, dest)
                    return
                else:
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j


def visualize_grid(grid, src, dest):
    root = tk.Tk()
    root.title("A* Pathfinding Visualization")
    canvas = tk.Canvas(root, width=COL * CELL_SIZE, height=ROW * CELL_SIZE)
    canvas.pack()

    for i in range(ROW):
        for j in range(COL):
            color = "white" if grid[i][j] == 1 else "black"
            canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE, (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE, fill=color)

    canvas.create_rectangle(src[1] * CELL_SIZE, src[0] * CELL_SIZE, (src[1] + 1) * CELL_SIZE, (src[0] + 1) * CELL_SIZE,
                            fill="green")
    canvas.create_rectangle(dest[1] * CELL_SIZE, dest[0] * CELL_SIZE, (dest[1] + 1) * CELL_SIZE,
                            (dest[0] + 1) * CELL_SIZE, fill="red")

    root.update()
    a_star_search(canvas, grid, src, dest)
    root.mainloop()


def main():
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]
    src = (8, 0)
    dest = (0, 0)
    visualize_grid(grid, src, dest)


if __name__ == "__main__":
    main()