import time


def read_input(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            row = list(line.strip())
            if row:
                grid.append(row)

    start = [0, 0]

    for j, ch in enumerate(grid[0]):
        if ch == "S":
            start = (0, j)
            break
    return start, grid


def count_splits(start, grid):
    R, C = len(grid), len(grid[0])
    visited = set()
    splits = 0

    def dfs(i, j):
        nonlocal splits
        if not (0 <= i < R and 0 <= j < C):
            return

        if (i, j) in visited:
            return
        visited.add((i, j))

        ch = grid[i][j]

        if ch == "^":
            # beam stops and new beams spawn left + right
            splits += 1
            dfs(i, j - 1)
            dfs(i, j + 1)
        else:
            dfs(i + 1, j)

    dfs(*start)

    return splits


if __name__ == "__main__":
    start = time.perf_counter()
    s, g = read_input("input.txt")
    print(f"Number of splits: {count_splits(s, g)}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
