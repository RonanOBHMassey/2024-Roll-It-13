# Checks users enter yes (y) and no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not choose a valid response.")


# Main Routine
want_instructions = yes_no("Do you want to read the instructions? (Y/N)= ")
print(f"you chose {want_instructions}")

roll_again = yes_no("do you want to roll again? ")
print(f"you chose {want_instructions} to rolling again")