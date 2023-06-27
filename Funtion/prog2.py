def inter(p,n,r):
    inter=(p*r*n)/100
    print("Interset:",inter)
a=input("enter the name of the customer:")
b=int(input("enter the age of the customer:"))
h=input("enetr the gender of the customer(m/f):")
d=int(input("enter the amount :"))
e=int(input("enetr the numkber of the years:"))
if(b>=60):
      r=12
      inter(d,e,r)
elif(b<60 and h=="f"):
    r=10
    inter(d,e,r)
else:
    r=9
    inter(d,e,r)
    
