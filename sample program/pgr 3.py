speed=int(input("enter the wind speed in kilometer per hour = "))
temp=int(input("enter the temperature in degree celsius = "))
t=temp
v=speed
a=13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
b=round(a)
print("wind chill index=",b)
