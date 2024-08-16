# Property Decorator = Best way to use setter and getter in python
# By property Methods acts as an attribute.
# class Number:
#     def __init__(self, num1= 0, num2 = 0):
#         self.num1 = num1
#         self.num2 = num2
 
#     def div(self, x, y):
#         return x / y
       

# obj = Number()
# obj.num1 = 20
# obj.num2 = 10

# print(obj.num1)
# print(obj.num2)
# print(obj.div(30, 15))

# print(obj.__dict__)


# Using property method: 
#property allow to use method as attribute
class Student:
    def __init__(self, marks):
        self.__marks = marks
    
    def percentage(self):
        return (self.__marks/600)*100

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        self.__marks = value

S = Student(500)
print(S.marks)
S.marks = 300
print(S.marks)


print(S.percentage(), "%")




