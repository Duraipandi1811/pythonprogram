year=int(input("enter the year:"))
if(year%400==0):
    print("its an the leap year")
elif(year%100==0):
    print("its an not leap year")
elif(year%4==0):
    print("its an leap year")
else:
    print("it is an not leap year")
    
    
