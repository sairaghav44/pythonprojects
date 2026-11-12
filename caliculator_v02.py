import re

num1 = input("enter the 1st number : ")
num2 = input("enter the 2nd number : ")

operator = input("enter  a operator (+,-,*,/): ")

n1 =re.findall(r'\d+' , num1)
n2 =re.findall(r'\d+' , num2)

n1 = int(n1[0])
n2 = int(n2[0])

if operator == '+':
    result = n1 + n2
    print(round(result, 2))
elif operator == '-':
    result = n1 - n2
    print(round(result, 2))
elif operator == '*':
    result = n1 * n2
    print(round(result, 2))
elif operator == '/':
    result = n1 / n2
    print(round(result, 2))
else:
    print(f"the entered {operator} is an invalid operator")