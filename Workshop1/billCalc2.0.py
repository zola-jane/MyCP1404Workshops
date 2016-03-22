print("Electricity bill Estimator 2.0")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

centsPerkWh = 0

tariff = input("Which tariff? 11 or 31?")
while tariff != '11' and tariff != '31':
    print("Invalid number.")
    tariff = input("Which tariff? 11 or 31?")

if tariff == '11':
    centsPerkWh = TARIFF_11
else:
    centsPerkWh = TARIFF_31

dailyUsekWh = float(input("Enter daily use in kWh:"))
numberOfBillingDays = float(input("Enter number of billing days:"))

estimatedBill = centsPerkWh * dailyUsekWh * numberOfBillingDays

print("Estimated bill: $" + '{0:.2f}'.format(estimatedBill))
