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
                    if digits % 2 != 0:
                        continue
                    mid = digits // 2
                    if str(num)[0:mid] == str(num)[mid:]:
                        wrong_id_total += num

    return wrong_id_total


print(read_ranges())
