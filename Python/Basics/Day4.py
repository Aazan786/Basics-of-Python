#head tail program

# import random

# random_integer = random.randint(0,1)
# if random_integer ==1:
#     print("Heads call")
# else:
#     print("Tails") 

#Random quote generator
# from random_word import RandomWords
# r = RandomWords()
# w = r.get_random_word()
# print(w)

#loops
# lists
# name = input("Give me parameter ")
# name1 =name.split("a")
# print(name1[1])

# nested list

#Final project: Rock paper

import random

print("""************************************************************
Welcome to Rock Paper Scissors...
The rules are simple:
The computer and user choose from Rock, Paper, or Scissors.
Rock win against scissors.
Paper win against  rock.
and
Scissors win against paper.
You will play the computer...the first to reach 3 wins wins the match.
Good luck!
************************************************************
""")

rock =  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper =  '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissors =  '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

game_images = [rock, paper, scissors]   
user_choice = int(input("Please choose (0) Rock, (1) Paper, or (2) Scissors: \n"))

if (user_choice >= 3 or user_choice < 0):
    print("You entered in vaild number: You lose: ")
else: 
    print("You choose")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer choice")
    print(game_images[computer_choice])


    if (user_choice == 0 and computer_choice == 2) or \
        (user_choice == 1 and computer_choice == 0) or \
        user_choice == 2 and computer_choice == 1:
        print("You win!")

    elif (user_choice == 2 and computer_choice == 0) or \
        (user_choice == 0 and computer_choice == 1) or \
        user_choice == 1 and computer_choice == 2:
        print("You lose!")

    elif (user_choice == computer_choice):
        print("Game Tie")







