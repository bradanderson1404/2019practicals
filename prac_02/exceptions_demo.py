"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A Value error will occur when ever a non-numerical value is assigned to the numerator/denominator
2. When will a ZeroDivisionError occur?
    When the denominator is set to 0 which would force the program to divide by 0 (impossible)
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by adding a while loop to check the denominator isn't set to 0
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("Cannot divide by zero!")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")


main()
