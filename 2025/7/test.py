import time


def solve(lines):
    row = [char == "S" for char in lines[0]]
    splits = 0
    for line in lines[1:]:
        for i, char in enumerate(line):
            if char == ".":
                continue
            row[i - 1] += row[i]
            row[i + 1] += row[i]
            splits += row[i] > 0
            row[i] = 0
    return splits, sum(row)


with open("input.txt", "r") as file:
    lines = file.read().strip().split("\n")

if __name__ == "__main__":
    start = time.perf_counter()
    print(f"Number of splits: {solve(lines)}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
