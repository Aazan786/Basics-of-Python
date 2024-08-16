#Function objects which is used to acceses inner function outside of outer function
# It remember value of scope function

#print Even no using Closure

def fun1():
    num = 0
    def fun2():
        nonlocal num
        num +=2
        return num
        
    return fun2

Even = fun1()
print(Even())
print(Even())
print(Even())
print(Even())

Even1 = fun1()
print(Even1())

#nested function
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)