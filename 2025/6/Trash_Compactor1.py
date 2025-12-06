import time


def main(filename):
    with open(filename) as file:
        lines = file.readlines()

    operators = lines[-1].split()
    equations = [int(n) for n in lines[0].split()]

    for line in lines[1:-1]:
        for i, num in enumerate(line.split()):
            num = int(num)
            operator = operators[i]

            if operator == "*":
                equations[i] *= num
            else:
                equations[i] += num

    return sum(equations)


if __name__ == "__main__":
    start = time.perf_counter()
    print(f"Grand total: {main('input.txt')}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
