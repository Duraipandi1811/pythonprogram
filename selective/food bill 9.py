food=int(input("enter the food rating:"))
service=int(input("enter the service rating:"))
ambience=int(input("enter the ambience rating:"))
bill=int(input("enter the bill amount:"))
if(food==4 or food==5):
    if(service==4 or 5 and ambience==4 or 5): 
      tip=bill*0.1
      print("Tip:",tip)
    else:
        tip=bill*0.05
        print("Tip:",tip)

else:
    if(service==4 or 5 and ambience==4 or 5):
        tip=bill*0.05
        print("Tip:",tip)
    else:
        tip=bill*0.01
        print("Tip:",tip)
