"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""


def main():
    finished = False
    result = 0
    while not finished:
        try:
            result = int(input("Enter a number: "))
            finished = True
        except ValueError:
            print("Please enter a valid number!")

    print("Result is:", result)


main()
