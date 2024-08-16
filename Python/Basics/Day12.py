# Local and Global Space of Variable
#Number guessing game:

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! Answer is: {answer}")

def set_diffculity():
    level = input("Set the level: 'Easy' or 'Hard':- ")
    if level == "easy".lower():
        return EASY_LEVEL_TURNS
    elif level == "hard".lower():
        return HARD_LEVEL_TURNS

def game():
    print("""-----Welcome to number guessing game.
    Your have to enter lower bound number 
    and upper bound and then make guess.-----\n""")
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))
    answer = random.randint(lower, upper)

    turns = set_diffculity()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaning to guess the answer. ")
        guess = int(input("Make a Guess? "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You have out of guess. 'You lose'")
            return

game()