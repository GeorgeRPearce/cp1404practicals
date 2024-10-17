choice = ""
name = input("Enter name: ")
while choice.upper() != "Q":
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ")
    if choice.upper() == "G":
        print(f"Goodbye {name}")
    elif choice.upper() == "H":
        print(f"Hello {name}")
    elif choice.upper() == "Q":
        print("Finished")
    else:
        print("Invalid choice")
