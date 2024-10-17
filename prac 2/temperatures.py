MENU = "(C)elsius, (F)ahrenheit, (Q)uit"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            temperature = float(input('Enter temperature in Celsius: '))
            result = temp_conversion_celsius(temperature)
            print(f"Result: {result:.2f} F")
        elif choice == "F":
            temperature = float(input('Enter temperature in Fahrenheit: '))
            result = temp_conversion_fahrenheit(temperature)
            print(f"Result: {result:.2f}")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def temp_conversion_celsius(temperature):
    fahrenheit = temperature * 9.0 / 5 + 32
    return fahrenheit


def temp_conversion_fahrenheit(temperature):
    celsius = 5 / 9 * (temperature - 32)
    return celsius

main()