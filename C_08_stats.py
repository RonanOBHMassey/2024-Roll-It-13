# create lists to hold computer and user scores
user_scores = []
comp_scores = []

# loop 6 times - for testing purposes, ask user to enter
# the score of both computer and user for each round.
for items in range(0, 6):
    user_points = int(input("Enter the user score: "))
    comp_points = int(input("Enter the computer score: "))

    # add user score to list of user scores
    user_scores.append(user_points)
    comp_scores.append(comp_points)

# calculate the lowest, highest and average scores and display them.

# sort the lists
user_scores.sort()
comp_scores.sort()

# find lowest, highest and average scores
user_low = user_scores[0]
user_high = user_scores[-1]
user_average = sum(user_scores) / len(user_scores)

print("low ", user_low)
print("high ", user_high)
print("average ", user_average)