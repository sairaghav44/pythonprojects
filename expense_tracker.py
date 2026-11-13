import re
import math

print (f" Welcome to the Expense tracker :) ")
print  ("*"*36)

expenses = []

while  True:
    user_input = input("Enter 'Description : Amount' (or 'done') :")

    if user_input.lower() == "done" :
        break

    parts= user_input.split(":")
    description = parts[0].strip()
    amount = float(parts[1].strip())

    expense = {
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    for expense in expenses:
        print(f"{expense['description']} : {expense['amount']}")

total= 0
for expense in expenses:
    total += expense["amount"]
print (f"Your total is: {total}")