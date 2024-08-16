#callable function object which return callable
#Function used to modify behaviour of another function
#arguments always passes to inner function


def multiply(fun):
    def inner(x, y):
        fun(x, y)
        return x*y
    return inner
        
@multiply # add = multiply(add)
def add(x, y):
    return x + y
    
print(add(2,3))

#Multiple decorator on single function
def multiply(fun):
    def inner(x, y):
        fun(x, y)
        return x*y
    return inner

def power(fun):
    def wrapper(x,y): 
        return x**2 + y**2
        fun(x**2, y**2)
    return wrapper

@power
@multiply # add = multiply(add)
def add(x, y):
    return x + y
    
print(add(2,3))


#Decroter with parameter
def main(z):
    def multiply(fun):
        def inner(x, y):
            fun(x, y)
            return x*y + z
        return inner
    return multiply

@main(5) # add = multiply(add)
def add(x, y):
    return x + y
    
print(add(2,3))

# Decorators on Class Methods
def CheckNum(func):
    def inner(self):
        if self.num1 > 20:
            print("Number is correct")
        else:
            func(self)
    return inner

class Number:
    def __init__(self, num1):
        self.num1 = num1
        
    @CheckNum
    def PrintNum(self):
        print("Number Enter by user is: ", self.num1)

obj = Number(12)
obj.PrintNum()


 

