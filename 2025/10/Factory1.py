import time
from collections import deque

lights_goal = []
buttons = []
joltage = []


def parse_line(line):
    parts = line.split()

    bracket = parts[0][1:-1]

    parens_list = []
    for tok in parts[1:-1]:
        inner = tok[1:-1]  # strip parentheses
        nums = [int(x) for x in inner.split(",")]
        parens_list.append(nums)

    curly_inner = parts[-1][1:-1]
    curly_list = [int(x) for x in curly_inner.split(",")]

    return bracket, parens_list, curly_list


def read_input(filename):
    with open(filename, "r") as f:
        for l in f:
            l = l.strip()
            if not l:
                continue
            b, p, c = parse_line(l)
            lights_goal.append(b)
            buttons.append(p)
            joltage.append(c)


def min_presses_bfs(goal, button_masks, n):
    start = 0  # all lights off bitmask is 0
    if goal == start:
        return 0

    max_state = 1 << n  # 2 ^ n max amount of states (will most likely not reach this )
    visited = [False] * max_state
    dist = [0] * max_state

    q = deque()
    q.append(start)
    visited[start] = True
    dist[start] = 0

    while q:
        state = q.popleft()

        for mask in button_masks:
            nxt = state ^ mask
            if not visited[nxt]:
                visited[nxt] = True
                dist[nxt] = dist[state] + 1
                if nxt == goal:
                    return dist[nxt]
                q.append(nxt)

    return 0


def solve():
    total_presses = 0
    # for the goal, and possible buttons find the smallest amount of presses and add that to total
    for pattern, button_list in zip(lights_goal, buttons):
        n = len(pattern)

        # build goal bitmask
        goal = 0
        for i, ch in enumerate(pattern):
            if ch == "#":
                goal |= 1 << i

        # build button bitmasks
        button_masks = []
        for button in button_list:
            mask = 0
            for idx in button:
                mask |= 1 << idx
            button_masks.append(mask)

        presses = min_presses_bfs(goal, button_masks, n)

        total_presses += presses

    return total_presses


if __name__ == "__main__":
    start = time.perf_counter()
    read_input("input.txt")
    total = solve()
    print("Total: ", total)
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")

