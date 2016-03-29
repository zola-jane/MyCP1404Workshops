"""
Write a loop that prints US presidential election years every 4 years since 1788
Function that returns the average value of a list of numbers passed into it
Function that returns the median value (middle when sorted) of a list of numbers passed into it
"""

for year in range(1788,2016+1,4):
    print(year, end=" ")

def calc_average(numbers):
    """
    calculate average of passed in numbers list
    :param numbers: list of numbers
    :return: average of numbers as float
    """
    return sum(numbers) // len(numbers)     # integer division //

print(calc_average([6,8]))
print(calc_average(range(1788,2016+1,4)))

def calc_median(numbers):
    """
    middle value of list of numbers
    :param numbers:
    :return: 
    """
    middle_index = len(numbers) // 2
    return sorted(numbers[middle_index])     # sorted returns the numbers sorted without changing

print(calc_average([3,3,1]))