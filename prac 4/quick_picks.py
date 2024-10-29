import random

LENGTH = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    num_of_quick_picks = int(input("How many quick picks? "))
    while num_of_quick_picks > 0:
        num_of_quick_picks = int(input("How many quick picks? "))

    for i in range(num_of_quick_picks):
        quick_pick = []
        for j in range(LENGTH):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
