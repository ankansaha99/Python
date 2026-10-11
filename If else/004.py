name=input("Enter your name : ")
age=int(input("Enter your age : "))

if age>=18:
    print("Okay,",name," You can Enter in this site")
    varify=int(input("Press 1 for Varification or 0 for exit "))
    if varify==1:
        nid=int(input("Enter Your NID number : "))
        if nid>0:
            print("Connecting to server...\n404 Error...\nPlease Wait until the day before death \nCause This site Under Construction")
        else:
            print("It is the end, See you again")
    elif varify==0:
        print("Exit Done ")
    else:
        print("Please Enter 0 or 1")

else:
    print("Sorry, ",name,"Try again at 18 ")