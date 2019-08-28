LOWER = 33
UPPER = 127


def main():
    print("Welcome to the ASCII Table Converter")
    print("( T ) - To view the ASCII Table")
    print("( I ) - To convert ASCII Integers to Characters")
    print("( C ) - To convert Characters to ASCII Integers")
    print("( Q ) - Quit")

    choice = str(input(">>> ")).upper()
    while choice != "Q":
        if choice == "T":
            for i in range(33, 128):
                letter = chr(i)
                print("{0:<3} : {1:>2}".format(str(i), letter))
            choice = str(input(">>> ")).upper()
        elif choice == "I":
            integer = int(input("Enter the ASCII Integer: "))
            while integer < LOWER or integer > UPPER:
                print("Integer must be between {0} and {1}".format(LOWER, UPPER))
                integer = int(input("Enter ASCII Integer: "))
            print("The ASCII Integer for the Character {0} is {1}"
                  .format(integer, chr(integer)))
            choice = str(input(">>> ")).upper()

        elif choice == "C":
            character = input("Enter any character: ")
            print("The Character {0} corresponds to the ASCII Integer of {1}"
                  .format(character, ord(character)))
            choice = str(input(">>> ")).upper()
        else:
            print("Invalid menu selection! Please select a valid option.")
            choice = str(input(">>> ")).upper()

    print("Finished.")


main()
