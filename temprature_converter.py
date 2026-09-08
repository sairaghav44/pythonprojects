#temp converter 
# #exercise 3 
#day 5

unit = input ("is this temperature in Celsious or Farenheight ? ( C/F):")
temp = float(input("enter the temprature : " ))

if unit == "C":
    temp = (temp * 9/5) + 32
    print(f"the temprature in Farenheight is {temp}F:")

elif unit == "F":
    temp = (temp - 32) * 5/9
    print(f"the temprature in Celsious is {temp}C:")

else:
    print(f"the entered unit '{unit}' is not a valid!")