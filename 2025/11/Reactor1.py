import time, collections


server_rack = collections.defaultdict(list)


def read_input(filename):
    with open(filename, "r") as f:
        for l in f:
            l = l.strip().split()
            k = l[0][:-1]
            for v in l[1:]:
                server_rack[k].append(v)


def get_paths(graph, start, end):
    visited = set()
    return dfs(start, end, graph, visited)


def dfs(u, end, graph, visited):
    if u == end:
        return 1
    visited.add(u)
    total = 0

    for v in graph.get(u, []):
        if v not in visited:
            total += dfs(v, end, graph, visited)

    visited.remove(u)  # have to BACKTRACK
    return total


if __name__ == "__main__":
    start = time.perf_counter()
    read_input("input.txt")
    # for k, v in server_rack.items():
    #     print(k, ": ", v)
    paths = get_paths(server_rack, "you", "out")
    print(f"Number of paths: {paths}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
