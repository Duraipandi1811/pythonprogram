name=input("enter the name:")
age=int(input("enter the age:"))
gender=input("enter the gender:")
number_of_days=int(input("enter the number of days:"))
if(age>=18 and age<=30):
   if(gender=='m'):
        wages=number_of_days*700
        print("wages:",wages)
   else:
        wages=number_of_days*700
        print("wages:",wages)
elif(age>=30 and age<=40):
    if(gender=='m'):
        wages=number_of_days*800
        print("wages:",wages)
    else:
        wages=number_of_days*800
        print("wages:",wages)
else:
    print("you enter the invalid.....")
        

        
           
