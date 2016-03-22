print("Body Mass Index Calculator, by Zola")

weight = float(input("Please enter your weight in kgs:"))
height = float(input("Please enter you height in m:"))

bmi = weight / height**2

print("Therefore your BMI value is", bmi, "\nThank you!")
