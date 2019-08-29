def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]

    # Will print the first integer in the list -> 3
    print(numbers[0])

    # Will print the first integer in the list going reverse -> 2
    print(numbers[-1])

    # Will print the 4th integer in the list -> 1
    print(numbers[3])

    # Will print from the start excluding the last integer (stop point) -> 3, 1, 4, 1, 5, 9
    print(numbers[:-1])

    # Will print starting from the 4th integer and stopping before the 5th -> 1
    print(numbers[3:4])

    # Will return true
    if 5 in numbers:
        print("True")
    else:
        print("False")

    # Will return false
    if 7 in numbers:
        print("True")
    else:
        print("False")

    # Will return true
    if "3" in numbers:
        print("True")
    else:
        print("False")

    # Will append 6, 5, 3 to the end of the list
    numbers + [6, 5, 3]
    print(numbers)

    numbers[0] = 10
    numbers[-1] = 1
    print(numbers[2:])
    if 9 in numbers:
        print("9 is an element.")
    print(numbers)


main()
