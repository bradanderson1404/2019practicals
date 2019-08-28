def main():
    min_length = int(input("Enter Password Length: "))
    password = get_password(min_length)
    for char in password:
        print("*", end='')


def get_password(min_length):
    password = input("Enter Password: ")
    while len(password) < min_length:
        print("Password is too short.")
        password = input("Enter Password: ")
    return password


main()
