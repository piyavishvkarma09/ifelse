print("good morning start your day")
user=input("morninng")
if user=="yes":
    print("good morning you can start your day")
    time=int(input("what time it is"))
    if time==6:
        print("morning excercise")
        excercise=input("did you go for excercise")
        if excercise =="yes":
            print("great")
            code=int(input("coding time"))
            if code>=8 and code<=12:
                print("codeing time")
                wtime=int(input("enter the time"))
                if wtime>=1 and wtime<3:
                    print("lunch time")
                    if wtime>=5 and wtime<= 6:
                        print("culture activity")
                        a=int(input("enter time"))
                        if a>=6 and a<=9:
                            print("coding")
                            if a>=9 and a<=11:
                                print("have your dinner")
                            else :
                                print("sleeping time")
                        else :
                            print("dinner")                       
                    else:
                        print("coding")                  
                else:
                    ("coding")
            else:
                print("other activity")
        else:
            print("you'll get oil") 
    else:
        print("you'll get oil")
else:
    print("what time it is")
