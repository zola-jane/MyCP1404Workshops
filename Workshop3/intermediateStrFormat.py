def main():
    lower = 10
    upper = 50
    number = get_number(lower, upper)

    # adjust to remove whitespace around the user's input string
    # word = "Hello!..."
    # print(word.strip(".!"))  # strips !...

    # write code that displays a table with two columns for ASCII and character
    # for i in range(10, 120, 11):  # make sure we have integers of different length
    #     print("{:^4d} | {:^4s}".format(i, chr(i)))


def get_number(lower, upper):
    finished = False
    while not finished:
        try:
            num = int(input("Enter a number ({}-{}):".format(lower,upper)))
            if num < lower or num > upper:
                print("Enter a valid number!")
            else:
                finished = True
        except:
            print("Enter a valid number!")
    return num



main()
