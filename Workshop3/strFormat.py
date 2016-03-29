name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

# The 'old' manual way to format text:

print("My guitar: " + name + ", first made in " + str(year))

# a better way using str.format():

print("My guitar: {}, first made in {}" .format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My guitar: {0} was first made in {1} (that's right, {1}!)" .format(name, year))

# Formatting currency:

print("My {} would cost ${:,.2f}" .format(name, cost))

# Aligning columns:

numbers = [1, 9, 123, 145, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}" .format(i + 1, numbers[i]))
