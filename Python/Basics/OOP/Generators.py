def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

my_gen = my_generator(3)
print(next(my_gen))
