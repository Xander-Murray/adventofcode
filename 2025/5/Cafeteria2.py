import time


def read_data(filename):
    ranges = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            a, b = line.split("-")
            ranges.append((int(a), int(b)))

    return ranges


def merge_ranges(ranges):
    ranges = sorted(ranges)
    merged = []

    for a, b in ranges:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            if b > merged[-1][1]:
                merged[-1][1] = b

    return merged


def check_valid(ranges):
    valid = 0
    merged = merge_ranges(ranges)

    for l, h in merged:
        valid += (h - l) + 1

    return valid


if __name__ == "__main__":
    start = time.perf_counter()
    r = read_data("input2.txt")
    print(f"Total valid ingredients: {check_valid(r)}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
