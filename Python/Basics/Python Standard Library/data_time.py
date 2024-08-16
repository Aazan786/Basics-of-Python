from time import time

start = time()
for i in range(10):
    print(i)
end = time()
print(f" Runtime of program is", end - start)
