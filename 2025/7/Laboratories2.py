import time


def read_input(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            row = list(line.strip())
            if row:
                grid.append(row)

    start = (0, 0)
    for j, ch in enumerate(grid[0]):
        if ch == "S":
            start = (0, j)
            break

    return start, grid


def count_timelines(start, grid):
    R, C = len(grid), len(grid[0])
    memo = {}

    def paths(i, j):
        # check bounds if we are still in we add 1
        if not (0 <= i < R and 0 <= j < C):
            return 1

        # simple memo
        if (i, j) in memo:
            return memo[(i, j)]

        ch = grid[i][j]

        memo[(i, j)] = res = (
            (paths(i, j - 1) + paths(i, j + 1)) if ch == "^" else paths(i + 1, j)
        )

        return res

    return paths(start[0], start[1])


if __name__ == "__main__":
    start = time.perf_counter()
    s, g = read_input("input.txt")
    print(f"Number of splits: {count_timelines(s, g)}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
