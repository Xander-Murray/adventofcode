import time


def read_data(filename):
    ranges = []
    ingredients = []
    reading_ranges = True

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                reading_ranges = False
                continue

            if reading_ranges:
                a, b = line.split("-")
                ranges.append((int(a), int(b)))
            else:
                ingredients.append(int(line))

    return ranges, ingredients


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


def bisect_right(arr, target):
    lo, hi = 0, len(arr)

    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid

    return lo


def check_valid(ranges, ingredients):
    merged = merge_ranges(ranges)
    starts = [a for a, _ in merged]

    valid = 0
    for num in ingredients:
        pos = bisect_right(starts, num)
        idx = pos - 1

        if idx < 0:
            continue

        lo, hi = merged[idx]
        if lo <= num <= hi:
            valid += 1

    return valid


if __name__ == "__main__":
    start = time.perf_counter()
    r, i = read_data("input.txt")
    print(f"Total valid ingredients: {check_valid(r, i)}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
