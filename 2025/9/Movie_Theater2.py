from itertools import combinations, pairwise
import time


def read_points(filename):
    with open(filename) as f:
        return [tuple(map(int, line.split(","))) for line in f if line.strip()]


def normalize_rect(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    left = min(x1, x2)
    right = max(x1, x2)
    bottom = min(y1, y2)
    top = max(y1, y2)
    return (left, bottom), (right, top)


def build_edge_boxes(points):
    # close the polygon loop
    loop = points + [points[0]]

    edge_boxes = []
    for p1, p2 in pairwise(loop):
        edge_boxes.append(normalize_rect(p1, p2))
    return edge_boxes


def rect_area_inclusive(rect):
    (x1, y1), (x2, y2) = rect
    return (x2 - x1 + 1) * (y2 - y1 + 1)


def edge_cuts_rectangle(rect, edge_rect):
    (x1, y1), (x2, y2) = rect  # box
    (p, q), (r, s) = edge_rect  # edge box

    # the edge is completely left/right/above/below, it doesn't cut it.
    return (
        p < x2
        and r > x1  # overlaps in x
        and q < y2
        and s > y1
    )  # overlaps in y


def solve(points):
    edge_boxes = build_edge_boxes(points)

    max_inside = 0  # max rectangle with no edges cutting through

    # all rectangles from pairs of vertices
    for p1, p2 in combinations(points, 2):
        rect = normalize_rect(p1, p2)
        area = rect_area_inclusive(rect)

        # only consider if it could beat current best
        if area > max_inside:
            # ceck every edge, if any edge cuts the interior not good box
            for edge_rect in edge_boxes:
                if edge_cuts_rectangle(rect, edge_rect):
                    break
            else:
                # no edge cut this rectangle so its  valid
                max_inside = area

    return max_inside


if __name__ == "__main__":
    start = time.perf_counter()
    points = read_points("input.txt")
    print(f"Biggest box possible: {solve(points)}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")

