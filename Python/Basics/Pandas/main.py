# with open("weather_data.csv") as filedata:
#     data = filedata.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as filedata:
#     data = csv.reader(filedata)
#     temperature = []
#     for i in data:
#         temperature.append(int(i[1]))
#     print(temperature)
    
import pandas as pd 
data = pd.read_csv("squirrel.csv")
# temp_list = data["temp"].tolist()
# # sum = 0
# for i in temp_list:
#    sum += i
# size = 0
# for j in temp_list:
#    size += 1
# average = sum/size
# print(int(average))

# average= data["temp"].mean()
# print(average)
# maximum = data["temp"].max()
# print(maximum)

#get data in row
# print(data[data.temp == data.temp.max()])

#Creating Dataframes form scratch

grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Blacl"])

data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



