# in this que we find out fierst and last digit and then print sum both of digits. 
n=int(input("enter the number:"))
f=n
if f>=10:
    # f=f//10
    print("first digit number",f//10)
if n%10:
    print("last digit",n%10)
# s=0
sum=(f//10+n%10)
print(sum)
