# while True:
#     try:
#        age = int(input("Enter your age: "))
#        xfactor = 10/age
#        print(xfactor)
#        print(age)
#     except (ValueError, ZeroDivisionError):
#         print("Enter valid arguments")
#     else:
#         print("No exceptions thrown")
#         break

#finally keyword is used to close resources like database, network, files etc
#wihh keyword is used to release the resources automatically
# while True:
#     try:
#        file = open("exceptions.py")
#        age = int(input("Enter your age: "))
#        xfactor = 10/age
#        print(xfactor)
#        print(age)
#     except (ValueError, ZeroDivisionError):
#         print("Enter valid arguments")
#     else:
#         print("No exceptions thrown")
#         break
#     finally:
#         file.close()

#Raise Exception => Costly
def division(a,b):
    if b<= 0:
        raise TypeError("Enter value of 'b' greater than 0")
    return a/b
try:
    division(10, 0)
except TypeError as error:
    print(error)