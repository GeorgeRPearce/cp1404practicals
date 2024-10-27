"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when any value entered is not an integer for example "A" or 0.1
2. When will a ZeroDivisionError occur?
when either the denominator or the numerator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0 or numerator == 0:
        print("Invalid")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")