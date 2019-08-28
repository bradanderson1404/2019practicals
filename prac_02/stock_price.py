import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_prices.txt"


def main():

    price = INITIAL_PRICE
    day = 0

    output_file = open(OUTPUT_FILE, 'w')

    print("Starting price: ${:,.2f}".format(price), file=output_file)

    while price >= MIN_PRICE and price <= MAX_PRICE:
        price_change = 0
        day += 1
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print("On day {} price is: ${:,.2f}".format(day, price), file=output_file)

    output_file.close()


main()
