import time, math
from itertools import combinations


# MY VERSION after learning about kruskal algorithm and disjoint set Data Structures
def get_dist(c1, c2):
    return math.dist(c1, c2)


class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        self.make_set(a)
        self.make_set(b)

        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False  # already same component

        # union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def component_sizes(self, points):
        # ensure to look at roots for exactly these points
        roots = {}
        for p in points:
            r = self.find(p)
            roots[r] = self.size[r]
        return list(roots.values())


def process(points, num_connections=0):
    # creates list of tuples for every combinations of 2 points
    combos = combinations(points, 2)
    # distances is list of tuples(distance between two points, point 1, point 2) for every combo in combos
    distances = [(get_dist(a, b), a, b) for a, b in combos]

    distances.sort()  # will sort by the distance ascending

    # Part1: optionally restrict to first num_connections edges
    if num_connections > 0:
        distances = distances[:num_connections]

    dsu = DSU()
    # every point starts as its own single component
    for p in points:
        dsu.make_set(p)

    # iterate over every tuple in distances
    # _ is distance, p is point one , q is point two
    for _, p, q in distances:
        dsu.union(p, q)

        # Part 2: early stop when everything is connected
        if num_connections == 0:
            roots = {dsu.find(pt) for pt in points}
            if len(roots) == 1:  # only one component, contains all points
                return p[0] * q[0]

    # Part 1
    # sort the lengths of the networks (components) and multiply the 3 biggest
    sizes = sorted(dsu.component_sizes(points), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def read_coords(filename):
    return [
        tuple(map(int, line.strip().split(",")))
        for line in open(filename)
        if line.strip()
    ]


if __name__ == "__main__":
    start = time.perf_counter()
    coords = read_coords("input.txt")
    # part 1
    # print(process(coords, 1000))
    # part 2
    print(
        process(
            coords,
        )
    )
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
