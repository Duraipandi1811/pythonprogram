import math
number=int(input("enter the number:"))
root=math.sqrt(number)
if int(root)**2==number:
    print(number,"Is a perfect square")
else:
    print(number,"Is not a perfect square")
