#cache maintain once in a program run
from functools import lru_cache
import time

@lru_cache(maxsize= None)
def myfun(n):
    time.sleep(3)
    return n*2

print(myfun(5))
print("Done for 5")
print(myfun(10))
print("Done for 10")
print(myfun(15))
print("Done for 15")
print("\n")
print(myfun(5))
print("Done for 5")
print(myfun(10))
print("Done for 10")
print(myfun(15))
print("Done for 15")
print("\n")
print(myfun(5))
print("Done for 5")
print(myfun(10))
print("Done for 10")
print(myfun(15))
print("Done for 15")