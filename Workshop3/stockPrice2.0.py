"""
CP1404/CP5632 Workshop 03 example
Capitalist Conrad wants us to write a stock-price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is a 50% chance it increases by 0 to 10%,
and a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""


def main():
    import random

    __author__ = 'Lindsay Ward'
    MAX_INCREASE = 0.175  # 17.5%
    MAX_DECREASE = 0.05  # 5%
    MIN_PRICE = 1.0
    MAX_PRICE = 100.0
    INITIAL_PRICE = 10.0

    count = 0
    price = INITIAL_PRICE
    print("Starting price:", format_currency(price))

    while price >= MIN_PRICE and price <= MAX_PRICE:
        priceChange = 0
        # generate a random integer of 1 or 2
        # if it's 1, the price increases, otherwise it decreases
        if random.randint(1, 2) == 1:
            # generate a random floating-point number
            # between 0 and MAX_INCREASE
            priceChange = random.uniform(0, MAX_INCREASE)
        else:
            # generate a random floating-point number
            # between negative MAX_INCREASE and 0
            priceChange = random.uniform(-MAX_DECREASE, 0)
        count += 1
        price *= (1 + priceChange)
        print("On day {} price is: {}".format(count, format_currency(price)))


def format_currency(value):
    return "${:,.2f}".format(value)


main()
