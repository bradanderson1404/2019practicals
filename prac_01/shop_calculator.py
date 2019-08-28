def main():
    items = []
    number_of_items = int(input("Number of items? "))
    while number_of_items < 0:
        print("Invalid number of items.")
        number_of_items = int(input("Number of items? "))
    for i in range(number_of_items):
        price = float(input("Enter item price: "))
        items.append(price)
    total = sum(items)
    if sum(items) > 100:
        total = total * 0.90
    print("Total price for", number_of_items, "items is: ${:.2f}".format(total))


main()
