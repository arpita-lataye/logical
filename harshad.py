a=int(input("enter the number:"))
i=a
sum=0
while i>0:
    sum=sum+(i%10)
    i=i//10
if a%sum==0:
    print("it is a harshad number")
else:
    print("it is not a harshad number")

# harshad number means addition of digits divide by user number