import random


# generate an integer between 0 and 6
# to simulate the roll of a die.
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice and returns total whether we had a double roll
def two_rolls(who):
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity.
    if roll_1 == roll_2:
        double_score = "yes"

    # find total points (so far)
    first_points = roll_1 + roll_2

    # show the user the result
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score



# main routine goes here
print("press <enter> to start this round: ")
input()

# get initial dice rolls for user
user_first = two_rolls("User")
user_points = user_first[0]
double_points = user_first[1]

double_feedback = ""

# tell user if they are eligible for double points
if double_points == "yes":
    double_feedback = "If you win this round, you get Double Points!"


# outputs initial move results
print(f"You rolled a total of {user_points}. {double_feedback}")
print()

# get initial dice rolls for computer
computer_first = two_rolls("computer")
computer_points = computer_first[0]

print(f"The computer rolled a total of {computer_points}.")

# loop (while both user / computer have < 13 points)
while computer_points < 13 and user_points < 13:

    # ask user if they want to roll again, update points / status
    print()
    roll_again = input("Do you want to roll the dice again? (type no to move it computer's turn)")
    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move

        # lets user know if you go over 13 and have lost
        if user_points > 13:
            print(f"Oops! you got rolled {user_move} which in total is {user_points} "
                  f"which is more than 13 so you lose this round"
                  f"and no points are added to your score.")

            # reset user points to zero so when we update their score at the end of the round, it is correct
            user_points = 0

            break

        else:
            print(f"You have rolled a {user_move}. you now have a total of {user_points} points.")

    # roll die for computer and update computer points
    computer_move = roll_die()
    computer_points += computer_move

    # if computer goes over.
    if computer_points > 13:
        print(f"The computer rolled a {computer_move}, "
              f"taking their points to {computer_points} "
              f"Which is more than 13 so... You Win!!! ")
        computer_points = 0
        break


    else:
        print(f"the computer rolled a {computer_move}, computer now has {computer_points}.")

    print()
    if user_points > computer_points:
        result = "You are ahead."
    elif computer_points > user_points:
        result = "The computer is ahead!"
    else:
        result = "Its a Tie!"

    print(f"***Round Update***: {result} ")
    print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}.")



# outside loop - double user points if they won and are eligible

# shows round results
if user_points < computer_points:
    print("Sorry, you have lost this round and no points have been added to your total score."
          f"the computer's score has increased by {computer_points} points. ")
    print("(⌐■_■)▄︻デ══━一💥           ○|￣|_")
else:
    if double_points == "yes":
        user_points *= 2

    print(f"Alright! you have won this round and {user_points} have been added to your total score!")
    print("o(~^▽^~)o (╬⌐■-■)")



