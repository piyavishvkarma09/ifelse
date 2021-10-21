alphabet=(input("enter the aphabet :"))
charector=(input("enter the charector :"))
number=int(input("enter the number : "))
if alphabet>="a"or alphabet<="z" and alphabet>="A" or alphabet<="Z":
    print("alphabet")
    if charector=="@" or charector=="#":
        print("charector")
        if number>=1:
            print("number")
        else:
            print("no number")
    else:
        print("no charector")
else:
    print("no alphabet")