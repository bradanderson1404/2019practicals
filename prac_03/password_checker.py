def main():
    min_length = int(input("Enter Password Length: "))
    password = input("Enter Password: ")
    while len(password) < min_length:
        print("Password is too short.")
        password = input("Enter Password: ")
    for char in password:
        print("*", end='')


main()
