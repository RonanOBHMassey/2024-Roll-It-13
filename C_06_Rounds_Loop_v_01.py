
# checks that users enter an integer
# that is more than 13
def int_check(question):

    while True:

        error = "Please enter an integer more than 13 or with out a decimal point."

        try:
            response = int(input(question))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)

            return response

        except ValueError:
            print(error)


# main routine goes here

# initialize user score and computer score
user_score = 0
comp_score = 0

target_score = int_check("Enter a target score: ")
print(target_score)

while user_score < target_score and comp_score < target_score:
    print("Round heading goes here...")
    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")
