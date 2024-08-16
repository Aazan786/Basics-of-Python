foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to purchase: (q = quit) ")
    if food == "q".lower():
        break
    else:
        price = int(input(f"Enter the price for {food}:"))
        foods.append(food)
        prices.append(price)

print("-----Your Cart-----")
for food in foods:
    print(food, end = " ,")
print()    
for price in prices:
    total += price
print(f"Your total bill is only/- {total}")    

    
   
       