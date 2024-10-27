FILENAME = "name.txt"
name = input("What is your name? ")
outfile = open(FILENAME, "w")
print(name, file=outfile)
outfile.close()

infile = open(FILENAME, "r")
name = infile.read().strip()
infile.close()
print(f"Hi {name}")

FILENAME = "numbers.txt"
with open(FILENAME, "r") as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
print(number_1 + number_2)

total = 0
with open(FILENAME, "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)