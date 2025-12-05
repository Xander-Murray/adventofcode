import time

# add to a list the ones to remove after esiting the search, keep searching until
# the list is completley empty meaning there is no more possible spots to check


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
    directions = [  # all of my possible adjacent directions
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    while True:
        to_remove = []

        for i in range(0, r_max):
            for j in range(0, c_max):
                adj_count = 0

                # check if its even worth checking adjacent spots
                if grid[i][j] == ".":
                    continue

                for di, dj in directions:
                    new_i = i + di
                    new_j = j + dj

                    # if we arent on the edge and we need to check all the spots for an '@'
                    if 0 <= new_i < r_max and 0 <= new_j < c_max:
                        if grid[new_i][new_j] == "@":
                            adj_count += 1

                if adj_count < 4:
                    # add the possittion of that cell to the remove list
                    # which means it was able to remove
                    to_remove.append((i, j))
        # we werent able to remove any so we are done
        # tp_total cant get bigger
        if not to_remove:
            break

        for i, j in to_remove:
            grid[i][j] = "."
            tp_total += 1

    print(f"Amount of TP: {tp_total}")


start_time = time.perf_counter()
main()
end_time = time.perf_counter()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"main() executed in {elapsed_time_ms:.2f} ms")
