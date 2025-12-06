import time


def main(filename):
    with open(filename) as file:
        lines = [line.rstrip("\n") for line in file]

    data = lines[:-1]
    last_line = lines[-1]
    final_eq = []
    operators = []

    max_width = max(len(row) for row in data)
    col = 0

    while col < len(last_line):
        # skip spaces to find the next operator
        while col < len(last_line) and last_line[col] == " ":
            col += 1
        if col >= len(last_line):
            break

        # this column has an operator
        problem_start_col = col
        op = last_line[problem_start_col]
        operators.append(op)

        problem_numbers = []

        while col < max_width:
            # are all number rows blank here?
            all_blank_nums = all(
                col >= len(data[row]) or data[row][col] == " "
                for row in range(len(data))
            )

            op_char = last_line[col] if col < len(last_line) else " "

            if all_blank_nums and op_char == " ":
                break

            num_str = ""
            for row in range(len(data)):
                if col < len(data[row]) and data[row][col] != " ":
                    num_str += data[row][col]

            if num_str:
                problem_numbers.append(int(num_str))

            col += 1

        final_eq.append(problem_numbers)

    results = []
    for op, new_nums in zip(operators, final_eq):
        if op == "*":
            prod = 1
            for n in new_nums:
                prod *= n
            results.append(prod)
        else:
            results.append(sum(new_nums))

    return sum(results)


if __name__ == "__main__":
    start = time.perf_counter()
    print(f"Grand total: {main('input.txt')}")
    end = time.perf_counter()
    print(f"{(end - start) * 1000:.2f} ms")
