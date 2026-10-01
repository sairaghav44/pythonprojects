import time

my_time = int( input("enter the time in seconds: "))

for x in range (my_time, 0,-1):
    seconds = x % 60
    minutes = int(x /60) %60
    hours = int(x/3600)
    print(f"{hours:02d}.{minutes:02d}.{seconds:02d}")
    time.sleep(1)

print ("TIMES UP!!!")