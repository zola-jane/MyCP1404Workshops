def main():
    print("Temperature Conversion Program")

    celsiusValue = float(input("Enter Celsius value:"))
    print("Celsius Value: {} degrees Celsius".format(celsiusValue))
    print("Fahrenheit Value: {} degrees Fahrenheit".format(calc_fahrenheit(celsiusValue)))
    print("Kelvin Value: {} Kelvin".format(calc_kelvin(celsiusValue)))


def calc_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def calc_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

main()
