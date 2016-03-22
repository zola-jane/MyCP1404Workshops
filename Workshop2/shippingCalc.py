'''work out total shipping charge for a number of items.
allow the user to enter the number of items and shipping cost per item.
compute and display the shipping cost.
if total shipping cost is over $100, a $10 discount is applied to the cost
'''

print("Shipping Cost Calculator")

numberOfItems = int(input("Enter number of items:"))
while numberOfItems < 0:
    print("Invalid number of items!")
    numberOfItems = int(input("Enter number of items:"))

totalCost = 0
discount = .10
for i in range(numberOfItems):
    itemCost = float(input("Enter shipping cost for item {}:".format(i+1)))
    totalCost += itemCost

if totalCost > 100:
    totalCost -= totalCost * discount

print("The total shipping cost is $" + '{0:.2f}'.format(totalCost))
