import time, collections

server_rack = collections.defaultdict(list)


def read_input(filename):
    with open(filename, "r") as f:
        for l in f:
            l = l.strip().split()
            k = l[0][:-1]
            for v in l[1:]:
                server_rack[k].append(v)


def get_paths_dp(graph, start, end):
    memo = {}

    def dfs(u, have_dac, have_fft):
        if u == "dac":
            have_dac = True
        if u == "fft":
            have_fft = True

        if u == end:
            return 1 if have_dac and have_fft else 0

        key = (u, have_dac, have_fft)
        if key in memo:
            return memo[key]

        total = 0
        for v in graph.get(u, []):
            total += dfs(v, have_dac, have_fft)

        memo[key] = total
        return total

    return dfs(start, False, False)


if __name__ == "__main__":
    start = time.perf_counter()
    read_input("input.txt")
    paths = get_paths_dp(server_rack, "svr", "out")
    print(f"Number of paths: {paths}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")

