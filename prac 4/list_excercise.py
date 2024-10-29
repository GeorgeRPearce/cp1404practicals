USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

number = [int(input('Number: ')) for count in range(5)]
print(f"The first number is {number[0]}")
print(f"The last number is {number[-1]}")
print(f"The smallest number is {min(number)}")
print(f"The largest number is {max(number)}")
print(f"The average of the numbers is {sum(number)/5}")

username = input("Enter username:")
if username in USERNAMES:
    print("Access granted")
else:
    print("Access denied")