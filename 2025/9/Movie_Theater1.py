from itertools import combinations
import time


def read_tiles(filename):
    return [
        tuple(map(int, line.strip().split(",")))
        for line in open(filename)
        if line.strip()
    ]


def area(a, b):
    x1, y1 = a
    x2, y2 = b

    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1

    return width * height


def main(tiles):
    pairs = (
        (area(a, b), a, b)
        for a, b in combinations(tiles, 2)
        if a[0] != b[0] and a[1] != b[1]
    )
    return max(pairs, key=lambda t: t[0])


if __name__ == "__main__":
    start = time.perf_counter()
    tiles = read_tiles("input.txt")
    print(main(tiles))
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
