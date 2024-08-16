import os

# Reading Writing files

# with open("azan.txt", "w") as file:
#     data = "Hi my name is azan"
#     file.write(data)

# with open("azan.txt", "r") as f:
#     print(f.read())

a = os.listdir("my folder")
for i in a:
    print(i)
