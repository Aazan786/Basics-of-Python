# @classmethods and @staticmethods
#class variable are shared by all objects of class 
# They can be called by objects or class itself
#class methods can be called by objects as well as class

class Students:
    counter = 0
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Students.counter =Students.counter + 1
    
    def msg(self):
        print(self.name + " " + "got" + " " + (str(self.marks)))

    @classmethod
    def object_count(cls):
        return cls.counter


std = Students("Azan", 200)
std1 = Students("Ahmed", 300)
std2 = Students("ali", 20)
print(Students.object_count())
