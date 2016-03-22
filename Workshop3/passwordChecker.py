MIN = 5  # minimum length of password
MAX = 15  # maximum length of password
SPECIAL_CHAR = "!@#$%^&*()-=_+`,~./'[]\<>?{}|"
uppercase = "1 or more uppercase characters"
lowercase = "1 or more lowercase characters"
number = "1 or more numbers"
special = "1 or more special characters:" + SPECIAL_CHAR


finished = False
while not finished:
    try:
        password = input(
        "Please enter a valid password:\nYour password must be between {} and {} characters, and contain:\n\t{}\n\t{}\n\t{}\n\t{}".format(
            MIN, MAX, uppercase, lowercase, number, special))
    except ValueError:
        print("Invalid character in your password")

    length = len(password)
    lower = sum([int(c.islower())for c in password])
    upper = sum([int(c.isupper()) for c in password])
    integer = sum([int(c.isdigit()) for c in password])
    special_char = sum(c in SPECIAL_CHAR for c in password)
    if length < MIN:
        print("Password is too short")
    elif length > MAX:
        print("Password is too long")
    else:
        if integer < 1:
            print("Password needs a number")
        elif upper < 1:
            print("Password needs an uppercase letter")
        elif lower < 1:
            print("Password needs a lowercase letter")
        elif special_char < 1:
            print("Password needs a special character")
        else:
            print("Your {}-letter password is valid: {}!".format(len(password),password))
            finished = True




