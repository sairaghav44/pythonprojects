#shopping cart programme 

foods= []
prices=[]
total =0 

while True:
    food= input("enter a food to buy (or type q to quit ) :")
    if food.lower() == 'q':
        break
    else :
        price =float(input (f"enter the price of {food} :"))
        foods.append(food)
        prices.append(price)

print("-----your cart-----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"your total is :{total:.2f}/-")
