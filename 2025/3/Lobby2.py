from termcolor import colored


def main():
    joltage = 0
    with open("input.txt", "r") as file:
        for line in file:
            # each battery is a line we need to get the largest 12 digits
            battery = [int(num) for num in line.strip()]

            # intuition is telling me that the original number i am checking against is the last 12 digits
            # and then starting from the leftmost digit see if we can find a max from that position to the left all the way
            #
            def get_12(battery):
                digits = [battery[-i] for i in range(12, 0, -1)]

                # for each digit starting from index 1 change it to the maximum
                # of the digits to the left bound up until including its sefl
                left_bound = 0
                curr_index = len(battery) - 12
                for i in range(len(digits)):
                    window = battery[left_bound : curr_index + 1]
                    best = max(window)
                    pos = left_bound + window.index(best)
                    left_bound = pos + 1  # plus 1 to exclude the left bound
                    digits[i] = best
                    # print(digits[i)
                    # left bound is the index of the last digit + 1
                    # the right bound includes the current digits
                    # index so it can get the max incase its already max
                    curr_index += 1
                return digits

            digis = get_12(battery)

            # digits is the list and when joined will be the jolts
            jolts = int("".join(str(num) for num in digis))

            joltage += jolts

            print(
                colored(
                    f"Battery: {''.join(str(num) for num in battery)}",
                    "white",
                    "on_green",
                )
            )
            print(colored(f"Jolts for this Battery: {jolts}", "white", "on_red"))

    print(f"Total Joltage: {joltage}")


main()
