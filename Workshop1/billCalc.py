print("Electricity bill Estimator")

centsPerkWh = float(input("Enter cents per kWh:"))
dailyUsekWh = float(input("Enter daily use in kWh:"))
numberOfBillingDays = float(input("Enter number of billing days:"))

estimatedBill = (centsPerkWh*.01) * dailyUsekWh * numberOfBillingDays

print("Estimated bill: $" + '{0:.2f}'.format(estimatedBill))
