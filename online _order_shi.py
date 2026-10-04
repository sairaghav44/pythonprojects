menu = { "pizza": 200,
          "burger": 150,
          "pasta": 180 ,
          "salad": 100,
          "soda": 50,
          "dessert" :120}

cart = []
total = 0


print ("-------------MENU-------------")
for key, value in menu.items():
    print(f"{key:10}: Rs {value}/- ")
print ("------------------------------")

while True:
    food = input("select a item(type q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-----------your cart----------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print()
print(f"Your total is : ERs {total}/-")