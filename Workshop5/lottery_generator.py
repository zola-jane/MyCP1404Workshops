"""
This program asks the user how many quick picks they wish to generate.
The program then generates that many lines of output.
Each line consists of siz random numbers between 1 and 45
Each line should not contain any repeated number.
Each line of numbers should be displayed in ascending order.
"""


def main():
    # lottery_numbers = []
    quick_pick = int(input("How many quick picks?"))

    for pick in range(quick_pick):
        lottery_numbers = get_random_numbers()
        print("{}".format(" ".join(str(i) for i in lottery_numbers)))


def get_random_numbers():
    import random
    numbers = []
    for number in range(6):
        number = random.randint(1, 45)
        while number in numbers:
            number = random.randint(1, 45)
        numbers.append(number)
    return numbers


main()
