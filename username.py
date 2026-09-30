#username 

username = input ("enter a username :   ")

if len(username) > 12 :
    print("your user name cannot contain more than 12 characters")
elif not username.find(" ")== -1:
    print("your yser name shouldnt contain any spaces")
elif not username.isalpha():
    print("your username should cant contain numbers or special characters")
else:
    print(f"welcome {username}")