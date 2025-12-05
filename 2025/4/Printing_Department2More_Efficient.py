import time
from collections import deque


def main():
    grid = []
    with open("input.txt") as f:
        for line in f:
            row = list(line.strip())
            if row:
                grid.append(row)

    r_max, c_max = len(grid), len(grid[0])

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    # create 2d array that will store the amount of adjacent tps around that particualr tp in adj[i][j]
    adj = [[0] * c_max for _ in range(r_max)]
    for i in range(r_max):
        for j in range(c_max):
            if grid[i][j] != "@":
                continue
            cnt = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < r_max and 0 <= nj < c_max and grid[ni][nj] == "@":
                    cnt += 1
            adj[i][j] = cnt

    q = deque()
    for i in range(r_max):
        for j in range(c_max):
            if grid[i][j] == "@" and adj[i][j] < 4:
                # add all of the tp's in which they are able to be removed since they are @ and their adj is under 4
                q.append((i, j))

    tp_total = 0

    while q:
        i, j = q.popleft()

        if grid[i][j] != "@":
            continue
        if adj[i][j] >= 4:
            continue

        grid[i][j] = "."  # change it to a period and add to tp_total
        tp_total += 1

        # the most important part is to change the count amoutn for all adj neighbors and if
        # one of those neighbors is now allowed to be removed we can add it to the queue
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < r_max and 0 <= nj < c_max and grid[ni][nj] == "@":
                adj[ni][nj] -= 1
                if adj[ni][nj] == 3:  # its now removable
                    q.append((ni, nj))

    print(f"Amount of TP: {tp_total}")


start = time.perf_counter()
main()
end = time.perf_counter()
print(f"{(end - start) * 1000:.2f} ms")
