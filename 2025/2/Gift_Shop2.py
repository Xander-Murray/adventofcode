import time


def read_ranges():
    wrong_id_total = 0
    with open("./input.txt", "r") as file:
        for line in file:
            for id_range in line.split(","):
                if not id_range.strip():
                    continue
                min_id = int(id_range[: id_range.find("-")])
                max_id = int(id_range[id_range.find("-") + 1 :])

                for num in range(min_id, max_id + 1):
                    digits = len(str(num))
                    mid = digits // 2
                    for i in range(1, mid + 1):
                        if digits % i == 0:  # multiple of length of full number
                            sub = str(num)[:i]
                            rebuild = sub * (digits // i)
                            if int(rebuild) == num:
                                wrong_id_total += num
                                break

    return wrong_id_total


start_time = time.perf_counter()
print(read_ranges())
end_time = time.perf_counter()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"my_function executed in {elapsed_time_ms:.2f} ms")
