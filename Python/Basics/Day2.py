name = len((input("what is your name\n")))
print(name)

Name = str(name)  #typecasting
print(type(Name))

var =str(123)        #typecasting
print(type(var))

print (type(70 + 100.5))
print(str(10) + str(10))

#Exercise
Number = input("Enter a two digit number ")

print(int(Number[0]) + int(Number[1]))

#BMI Calculator

Height = input("Enter height in m ")
Weight = input("Enter weght in kg ")

# Height_Result = float(Height) * float(Height)

BMI = int(Weight)/float(Height)**2
print(int(BMI))

# Tip Calculator
print("Welcome to tip calculator")
Total_bill = float(input("What was the total bill? $ "))
Tip = int(input("What percentage would you like to give tip? 10, 12 or 15? "))

amount_with_tip = Tip/100 *Total_bill + Total_bill

Total_people = int(input("How many people to split the bill? "))
Final_Bill = int(amount_with_tip/Total_people)

print(f"Total Bill to each person ${Final_Bill}")

# main learning: Type conversion and mathimatical expression, Input function type = str => inorder to perform operations
# on it we have to type cast it
 









