import random

MINIMUM = 1
MAXIMUM = 45


def main():
    total_quickpicks = int(input("How many quick picks would you like? "))
    for i in range(total_quickpicks):
        get_quick_picks()


def get_quick_picks():
    quick_picks = []
    while len(quick_picks) != 6:
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in quick_picks:
            quick_picks.append(number)
    quick_picks.sort()
    print(*quick_picks, sep=" ")


main()
