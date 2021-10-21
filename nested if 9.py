#facebook
fb=input("do you want to creat new account")
if fb=="no":
    print("log in")
    number=int(input("enter your number  or gmail"))
    if number>=99999999 or number<=9999999999:
        print("connecting")
        password=input("enter your password")
        if password=="naruto":
            print("you are logged in")
        else:
            print("wrong password")
    else:
        print("invalid connection")
else:
    print("create new acccount")
    

