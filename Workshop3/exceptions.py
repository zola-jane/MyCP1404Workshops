try:
    numerator = int(input("Enter the numerator:"))
    denominator = int(input("Enter the denominator:"))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
1. When will a ValueError occur? When the values entered is not the type specified.
2. When will a ZeroDivisionError occur? When the value for the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

