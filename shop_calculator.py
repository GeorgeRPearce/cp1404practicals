total = 0
number_of_items = int(input("Number of itens: "))
if number_of_items <= 0:
    while number_of_items <= 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of itens: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total = total + price
print(f"Total price for {number_of_items} items is {total:.2f}")