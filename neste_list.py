
a=[1,2,3,4,5,6,7,8,9,0,8,7,6,5,3]
n=[]
b=[]
count=0
for i in range(len(a)):
    if count==5:
        n.append(b)
        b=[]
        count=1
    else:
        count+=1
    b.append(a[i])
print(n)