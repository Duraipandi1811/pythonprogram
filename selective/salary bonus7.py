salary=int(input("enter the current amount:"))
work=int(input("enter the year of services:"))
if(work>10):
    bonus=salary*0.1
    print("The Bonus:",bonus)
elif(work<=10 and work>6):
    bonus=salary*0.8
    print("The Bonus:",bonus)
else:
    bonus=salary*0.05
    print("The Bonus:",bonus)
