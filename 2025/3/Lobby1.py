def main():
    joltage = 0
    with open("input.txt", "r") as file:
        for line in file:
            # each battery is a line we need to get the largest
            # number starting from the left and then find the next largest starting from that point
            battery = [int(num) for num in line.strip()]

            dig1 = max(battery[0:-1])
            start = battery.index(dig1)
            dig2 = max(battery[start + 1 :])

            jolts = int(f"{dig1}{dig2}")
            joltage += jolts

            print(
                f"Battery: {''.join(str(num) for num in battery)} | Jolts for this Battery: {jolts}"
            )

    print(f"Total Joltage: {joltage}")


main()
