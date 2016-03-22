""" open the file called "name.txt" and reads the name
and prints "Your name is " with the name in the file.
"""

in_file = open("name.txt", "r")
for line in in_file:
    print("Your name is ", line.strip())
