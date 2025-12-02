hit_zero = 0

lock = 50

with open("./input.txt", "r") as file:
    for line in file:
        line = line.strip()
        direction = line[0]
        amount = int(line[1:])

        if direction == "R":
            lock = (lock + amount) % 100
        else:
            lock = (lock - amount) % 100
        if lock == 0:
            hit_zero += 1

print(hit_zero)
