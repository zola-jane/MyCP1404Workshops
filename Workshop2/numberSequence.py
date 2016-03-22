"""
get x
get y
#could add a function that error checks the values for x and y

show menu
# add error checking for menu choice
# calculations are inclusive of the value of y
1. show even numbers from x to y
2. show odd numbers from x to y
3. show the squares from x to y
4. exit the program

"""

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
while y <= x:
    print("The value of y must be greater than x")
    x = int(input("Enter the value of x:"))
    y = int(input("Enter the value of y:"))


print("Menu choice:\n1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares from x to y\n4. Exit the program")
menuChoice = input("Enter menu choice:")
while menuChoice != "4":
    if menuChoice == "1":
        for i in range(x,y+1):
            if i % 2 == 0:
                print(i, end =' ')
    elif menuChoice == "2":
        for i in range(x,y+1):
            if i % 2 == 1:
                print(i, end=' ')
    elif menuChoice == "3":
        for i in range(x,y+1):
            print(i**2, end=' ')
    else:
        print("Invalid menu choice.")
    print("\nMenu choice:\n1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares from x to y\n4. Exit the program")
    menuChoice = input("Enter menu choice:")

print("Program finished")

