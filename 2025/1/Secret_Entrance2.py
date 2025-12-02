hit_zero = 0

lock = 50

with open("./input.txt", "r") as file:
    for line in file:
        line = line.strip()
        direction = line[0]
        amount = int(line[1:])
        extra = 0

        if direction == "R":
            to_zero = 100 - lock if lock > 0 else 100
            if amount >= to_zero:
                extra = 1 + (amount - to_zero) // 100
            lock = (lock + amount) % 100
        else:
            to_zero = lock if lock > 0 else 100
            if amount >= to_zero:
                extra = 1 + (amount - to_zero) // 100
            lock = (lock - amount) % 100
        hit_zero += extra

print(hit_zero)
