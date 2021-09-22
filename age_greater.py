age1=int(input("enter the first age:"))
age2=int(input("enter the second age:"))
age3=int(input("enter the third age:"))

if age1>age2 and age1>age3:
    print("age1 greater",age1)
elif age2>age3:
    print("age2 greater",age2)
else:
    print("age3 greater",age3)
