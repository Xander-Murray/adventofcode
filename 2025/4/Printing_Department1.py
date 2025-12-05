import time


def main():
    tp_total = 0
    grid = []

    with open("input.txt", "r") as file:
        # read in the input into a 2d array
        for line in file:
            row = list(line.strip())
            grid.append(row)

    # get r and c count next and the check each index
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
    for i in range(0, r_max):
        for j in range(0, c_max):
            cell = grid[i][j]
            adj_count = 0

            if cell == ".":
                continue
            # check if its even worth checking adjacent spots

            # if we arent on the edge and we need to check all the spots for an '@'
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj

                if 0 <= new_i < r_max and 0 <= new_j < c_max:
                    if grid[new_i][new_j] == "@":
                        adj_count += 1
            if adj_count < 4:
                tp_total += 1
    print(f"Amount of TP: {tp_total}")


start_time = time.perf_counter()
main()
end_time = time.perf_counter()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"main() executed in {elapsed_time_ms:.2f} ms")
