age=int(input("enter age:"))
if(age<18):
    print("you can't vote")
    print("you are child")
elif(age>18 and age<45):
    print("you are a adult")
else:
    print("you are old adult")