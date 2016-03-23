def main():
    print("Body Mass Index Calculator, by Zola")

    weight = float(input("Please enter your weight in kgs:"))
    height = float(input("Please enter you height in m:"))

    bmi = calc_bmi(weight, height)

    print("Therefore your BMI value is {:.2f}\nThank you!".format(bmi))


def calc_bmi(weight, height):
    body_mass_index = weight / height ** 2
    return body_mass_index


main()
