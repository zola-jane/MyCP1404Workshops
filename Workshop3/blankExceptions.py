finished = False
result = 0
while not finished:
    try:
        number = int(input("Enter a number: "))
        finished = number
    except ValueError:
        print("Please enter a valid integer")
print("valid result is", result)