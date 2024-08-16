#different method of creating list
numbers = list(range(10))
print(numbers)

chars = list("Azan Ali")
print(chars)

combined = numbers + chars
print(combined)

num = list(range(20))
print(num[:])

#list unpacking and packing: Store individual list item in a seperate variable = unpacking
#packing = store whole list in single variable
numbers = list(range(10))
first, second, * others = numbers
print(first)
print(second)
print(others)

#unpacking, unpack operator = *
def fun1(a,b,c,d): 
    print(a,b,c,d)

my_list = list(range(4))

fun1(*my_list)

#packing
def my_sum(*num):
    return sum(num)


output =my_sum(1,2,3,4,5)
print(output)

list_1 = [1,2,3,4,5,6]
list_2 = [8,5,4,3,2]
result = [*list_1, *list_2]
print(result)

dict_1 = {"x":1, "y": 3} 
dict_2 = {"z":2, "a": 4} 
result = {**dict_1, **dict_2}
print(result)

#sorting list
list= [
    ("Apple", 100),
    ("Mango", 200),
    ("Banana", 50),
    ("Pineapple", 150)
]

# def sort_item(list):
#     return list[1]

list.sort(key= lambda list:list[1])
print(list)


#Lambda function
list= [
    ("Apple", 100),
    ("Mango", 200),
    ("Banana", 50),
    ("Pineapple", 150)
]
list.sort(key= lambda list:list[1])
print(list)
map
items = [
    ("Apple", 100),
    ("Mango", 200),
    ("Banana", 50),
    ("Pineapple", 150)
]

prices = list(map(lambda item: item[1], items))
print(prices)

#filter
items = [
    ("Apple", 100),
    ("Mango", 200),
    ("Banana", 50),
    ("Pineapple", 150)
]

filtered = list(filter(lambda item: item[1]>= 100,items))
print(filtered)

my_list = [1,2,3,4,5,]
result = list(filter(lambda my_list: my_list % 2 == 0 , my_list))
print(result)

#reduce
from functools import reduce
items = [
    ("Apple", 100),
    ("Mango", 200),
    ("Banana", 50),
    ("Pineapple", 150)
]
filtered = list(map(lambda item: item[1],items))
sum = reduce(lambda x,y: x+y, filtered)
print(sum)

#enumerate
list = ["a", "b", "c", "d", "e", "f"]
for index, i in enumerate(list):
    print(index, i)

#Zip
username = ["Azan", "Ahmed", "Ali"]
password = ["abc", "xyz", "123"]

result = dict(zip(username, password))
for key in result:
   print(key, end=" ")
   print(result[key])

#list compression
students = [100,90,80,60,50,70,90,80]
result = [i for i in students if i >=70] #[expression for i in iterable condition]
print(result)

list = [i*2 for i in range(1,5)]
print(list)

with open("f1.txt") as file1:
    f1_data = file1.readline()
with open("f2.txt") as file2:
    f2_data = file2.readline()

result = [int(num) for num in f1_data if num in f2_data]
print(result)

#dict compression = {new key: expression for (kye,value) in iterable}
student_scores = {
    "Azan": 93,
    "Ali": 83,
    "Azam": 72,
    "Azani": 63,
    "Azlan": 50
}

percentage = {key: (value-200/100) for (key,value) in student_scores.items()}
print(percentage)

#Final Exercise: 
from pprint import pprint

sentence = "This is a common interview question"
char_frequancy = {}
for char in sentence:
    if char in char_frequancy:
        char_frequancy[char] +=1
    else:
        char_frequancy[char] = 1
#pprint(char_frequancy, width=2)

def sort(letter):
    return letter[1]

most_frequent =(sorted(char_frequancy.items(), key= sort, reverse=True)) 
print(most_frequent[0])

#2nd method

list = []
for i in char_frequancy:
    k = (i, char_frequancy[i])
    list.append(k)
list.sort(key=sort, reverse=True)
print(list[0])
