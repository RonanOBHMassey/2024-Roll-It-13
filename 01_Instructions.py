print(" o(^▽^)o 🎲🎲 Roll it 13! 🎲🎲 o(^▽^)o ")


# Loop for testing purposes.

while True:
    want_instructions = input("Do you want to read the instructions? (Y/N)= ").lower()

    # Checks users enter yes (y) and no (n)
    if want_instructions == "yes" or want_instructions == "y":
        print("you chose yes")
    elif want_instructions == "no" or want_instructions == "n":
        print("you chose no")
    elif want_instructions == "yesno" or want_instructions == "yn":
        print("you thought you were clever...")
        exit()
    else:
        print("You did not choose a valid response.")