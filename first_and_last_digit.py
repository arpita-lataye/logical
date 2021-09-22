
n=int(input("enter the number:"))
f=n
if f>=10:
    f=f//10
    print("first digit number",f//10)
if n%10:
    print("last digit",n%10)