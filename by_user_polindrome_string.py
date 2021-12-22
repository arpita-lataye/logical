a=input('enter string:')
length=len(a)
b=''
for i in range(len(a)):
    length=length-1
    b+=a[length]
print(b)
if b==a:
    print('polidrome')
else:
    print('not polidrome')