# EXERCISE-6
# Snake Water Gun Game Development.
# Game must be played for 10 times.
# have to count scores +1 for each wins and 0 for each lose.
# have to display how many times we and computer wins and have to display the winner.
# also print the number of choices left to the user.

# Hint - have to use random module and choice function of it.

import random

comp_wins = 0
user_wins = 0
play_chance = 10
left_chance = 1
draw_times = 0
i = 1
list = ["s", "w", "g"]
# print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLet's play Snake,Water,Gun Game")

print(f"{"\t"*16}Let's play Snake,Water,Gun Game\n")
print("For each wins you get +1 point and for each loose or draw you get 0 point")
print("Choose from the following: s,w,g")
print("s:snake\nw:water\ng:gun\n")

while left_chance <= play_chance:
    comp_choose = random.choice(list)
    user_choose = input(f"{i}). Snake,Water,Gun:")

    if comp_choose == user_choose:
        print("computer choosed",comp_choose)
        print("you choosed",user_choose)
        print("DRAW")
        draw_times += 1
        warn_chance = 10 - left_chance
        print(f"{warn_chance} chances left out of 10\n")

    elif comp_choose == "s" and user_choose == "w":
        print("computer choosed",comp_choose)
        print("you choosed",user_choose)
        print("Computer wins")
        comp_wins += 1
        warn_chance = 10 - left_chance
        print(f"{warn_chance} chances left out of 10\n")

    elif comp_choose == "s" and user_choose == "g":
        print("computer choosed",comp_choose)
        print("you choosed",user_choose)
        print("User wins")
        user_wins += 1
        warn_chance = 10 - left_chance
        print(f"{warn_chance} chances left out of 10\n")
    elif comp_choose == "w" and user_choose == "s":
        print("computer choosed",comp_choose)
        print("you choosed",user_choose)
        print("User wins")
        user_wins += 1
        warn_chance = 10 - left_chance
        print(f"{warn_chance} chances left out of 10\n")
    elif comp_choose == "w" and user_choose == "g":
        print("computer choosed",comp_choose)
        print("you choosed",user_choose)
        print("Computer wins")
        comp_wins += 1
        warn_chance = 10 - left_chance
        print(f"{warn_chance} chances left out of 10\n")
    elif comp_choose == "g" and user_choose == "s":
        print("computer choosed",comp_choose)
        print("you choosed",user_choose)
        print("Computer wins")
        comp_wins += 1
        warn_chance = 10 - left_chance
        print(f"{warn_chance} chances left out of 10\n")
    elif comp_choose == "g" and user_choose == "w":
        print("computer choosed",comp_choose)
        print("you choosed",user_choose)
        print("User wins")
        user_wins += 1
        warn_chance = 10 - left_chance
        print(f"{warn_chance} chances left out of 10\n")
    else:
        print(f"Please choose in small letters \ncapital S,W,G are not allowed \nchoose small case letters s,w,g\n")

    left_chance += 1
    i += 1

print(f"You wins {user_wins} times out of 10")
print(f"Computer wins {comp_wins} times out of 10")
print(f"Game gets draw {draw_times} times out of 10\n")

if user_wins == comp_wins:
    print("Game is DRAW between you and computer")
elif user_wins > comp_wins:
    print("YOU WON THE GAME")
else:
    print("COMPUTER WON THE GAME")