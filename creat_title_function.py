lis=["my name is aakshi"]
a=lis[0].split()
print(a)
d=[]
for i in range(len(a)):
    s=""
    for j in range(len(a[i])):
        if j==0:
           s+=a[i][0].upper()
        elif j!=0:
           s+=a[i][j]
    d.append(s)
print(d)