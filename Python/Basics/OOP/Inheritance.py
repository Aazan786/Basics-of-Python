 class Person:
#     def __init__(self, name, age):  # Constructor to initialize name and age attributes
#         self.name = name
#         self.age = age

def say_hello(self):  # Method to greet and introduce the person
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# class Student(Person):  # Student class inherits from Person class
#     def __init__(self, name, age, grade):  # Constructor to initialize name, age, and grade attributes
#        super().__init__(name, age)  # Call the parent class constructor to initialize name and age
#        self.grade = grade  # Additional attribute specific to the Student class

#     def say_hello(self):  # Override the say_hello method of the parent class
#         super().say_hello()  # Call the parent class say_hello method to introduce the student as a person
#         print(f"I am a student in grade {self.grade}.")  # Print additional information specific to the Student class

# # Creating an instance of the base class
# person = Person("John", 30)
# student = Student("Mary", 18, 12)
# print(isinstance(person, Student))
# print(isinstance(student, Person))
# print(isinstance(person, object))
# print(isinstance(student, object))
# print(issubclass(Person, object))


# class Department:
#     def __init__(self):
#         print("Parent Constructor")
#         self.name = "IT"
#         self.id = 34
    
#     def DeptFun(self):
#         print("Department Function")

# class Teacher(Department):
#     def __init__(self):
#         super().__init__()
#         print("child constructor")
#         self.name = "Azan"
#         self.salary= 34000
    
#     def TechFun(self):
#         print("Teacher Function")

# T = Teacher()
# print(T.id)
# print(T.salary)

#MultiLevel Inheritance: Avoid it, limit inheritance upto 1 or 2 level


# EXtending Built in Types 
# class Text(str):
#     def duplicate(self):
#         return self + self

# t = Text("Azan")
# print(t.capitalize())
# print(t.upper())
# print(t.duplicate())






