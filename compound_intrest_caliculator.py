 #compound intrest caliculator 

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle =float(input("enter the principle: "))
    if principle <= 0:
        print("principle shouldnt be less than or equal to zero:")

while rate <= 0:
    rate =float(input("enter the intrest rate: "))
    if rate <= 0:
        print("intrest rate shouldnt be less than or equal to zero:")

while time <= 0:
    time =float(input("enter the time in years: "))
    if time <= 0:
        print("time shouldnt be less than or equal to zero:")

total = principle * pow((1 + rate / 100), time)

#yaaa firsst time seeing the form

print(f" balance after {time} years is {total} :")