# original code
lower = 10
upper = 100

print("Enter a number (" + str(lower) + "-" + str(upper) + "):")

# rewrite with string formatting

print("Enter a number ({}-{}:)" .format(lower,upper))

# adjust to remove whitespace around the user's input string
# word = "Hello!..."
# print(word.strip(".!"))  # strips !...

# write code that displays a table with two columns for ASCII and character
for i in range(10, 120, 11):    # make sure we have integers of different length
    print("{:^4d} | {:^4s}".format(i, chr(i)))
