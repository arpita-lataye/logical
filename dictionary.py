a=[{'m':23,'b':45},{'m':55,'b':45}]
b=input('enter key:')
s=0
for i in range(len(a)):
    for j in a[i]:
        if j==b:
            s+=a[i][j]
print(s)