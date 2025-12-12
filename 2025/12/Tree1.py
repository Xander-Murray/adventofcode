import time

SIZES = {}
parts = []


def read_input(filename):
    global SIZES, parts

    with open(filename, "r") as f:
        parts = f.read().strip().split("\n\n")

    SIZES = {}

    # all blocks except last are presents
    for block in parts[:-1]:
        lines = block.splitlines()
        if not lines:
            continue

        present_id = int(lines[0].rstrip(":"))
        grid = lines[1:]

        size = sum(row.count("#") for row in grid)
        SIZES[present_id] = size


def main():
    ans = 0
    regions = parts[-1]

    present_ids = sorted(SIZES.keys())

    for line in regions.splitlines():
        if not line.strip():
            continue

        sz, counts_str = line.split(": ")
        R, C = map(int, sz.split("x"))
        counts = list(map(int, counts_str.split()))

        # counts[i] corresponds to present_ids[i]
        total_present_size = sum(
            counts[i] * SIZES[present_ids[i]] for i in range(len(present_ids))
        )
        total_grid_size = R * C

        if total_present_size * 1.3 < total_grid_size:
            ans += 1
        elif total_present_size > total_grid_size:
            pass

    return ans


if __name__ == "__main__":
    start = time.perf_counter()
    read_input("input.txt")
    print(f"Number of valid regions: {main()}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")

