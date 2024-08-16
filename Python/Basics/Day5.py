# Average in list

students_height = input("Enter list of students height ").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)    

Suum = 0
for i in students_height:
    Suum = Suum + i

length = 0
for j in students_height:
    length = length + 1

Average_height = round(Suum/length)
print(f"The average height is {Average_height}")

#max number is list

students_scores = input("Enter list of students height ").split()
for n in range(0, len(students_scores)):
     students_scores[n] = int(students_scores[n])
print(students_scores)    

max = students_scores[0]
for i in students_scores:
    if i > max:
        max = i
print(max)            


#fizzbuzz

for i in range(1, 101):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 5:
        print("buzz")
    elif i % 3 and i % 5 == 0:
        print("fizzbuzz")
    else:
        print(i)  

# Password genentator program:

#without user input

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
'H', 'I', 'J', 'K', 'L', 'M', 'N','z', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 
'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '<', '>', '?' ]

number_letters = int(input("How many letters would you like in your password? "))
number_symbols = int(input("How many symbols would you like in your password? "))
number_numbers = int(input("How many number would you like in your password? "))

password = []
for char in range(1, number_letters + 1):
    password += random.choice(letters)

for sym in range(1, number_symbols + 1):
    password += random.choice(symbols)

for num in range(1, number_numbers + 1):
    password += random.choice(numbers)

random.shuffle(password)
password_string = ""
for char in password:
    password_string += char

print(f"Your strong password is: {password_string}")    


# with user input
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
'H', 'I', 'J', 'K', 'L', 'M', 'N','z', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 
'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '<', '>', '?' ]

user_input = int(input("Enter length of your password? "))
while True:
 
    try:
 
        length = int(user_input)
 
        if length < 8:
 
            print("Your length of passwrd should be at least 8.")
 
            user_input = int(input("Please, Enter your number again: "))
 
        else:
 
            break
 
    except:
 
        print("Please, Enter numbers only.")
 
        user_input = int(input("How many characters do you want in your password? "))

# number_letters = int(input("How many letters would you like in your password? "))
# number_symbols = int(input("How many symbols would you like in your password? "))
# number_numbers = int(input("How many number would you like in your password? "))

part1 = round(length * (50/100))
part2 = round(length * (25/100))
part3 = round(length * (25/100))

password = []
for char in range(part1):
    password.append(letters[char])

for sym in range(part2):
    password.append(symbols[sym])

for num in range(part3):
   password.append(numbers[num])

random.shuffle(password)
password_string = ""
for char in password:
    password_string += char

print(f"Your strong password is: {password_string}")  



   