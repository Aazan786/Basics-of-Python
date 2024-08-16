#Leap year exercise
# Year = int(input("Enter the year you want to check? "))

# if Year % 4 == 0:
#     if Year % 100 == 0:
#         if Year % 400 == 0:
#             print(f"{Year} is a leap year")
#         else:
#             print(f"{Year} is not a leap year") 
#     else:
#          print(f"{Year} is a leap year")          
# else:
#     print(f"{Year} is not a leap year")

 # Pizza order exercise:

# print("Welcome to Azan Pizza shop")
# size = input("What size pizza do you want ? S, M or L \n")
# add_pepperoni = input("Do you want pepperoni ? Y or N \n")
# add_cheesse = input("Do you want extra cheese ? Y or N \n")

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:  
#     bill += 25  

# if add_pepperoni == "Y":
#     if size == "S":
#        bill += 2
#     else:
#         bill +=3

# if add_cheesse == "Y":
#     bill += 1

# print(f"Your final bill is {bill}$")    

# Final Task:
print("Welcome to treasure island")
print("Your job is to find the treasure")

choice1 = input("you are at road! where you want to go left or right  ").lower()


if choice1 == "left":
    choice2= input("Do you want to swim or wait for boat  ").lower()
    if choice2 =="wait":
        choice3 = input("Which color you want to choose red yellow or blue  ").lower()
        if choice3 == "yellow":
            print("You find treasure")
        elif choice3 == "red":
            print("oopps try again")  
        elif choice3 == "blue":
            print("bad luck")    
    else:
        print("game over")
else:
    print("game over")    


#learning: lower(), nested control flow.








