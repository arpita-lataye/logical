a=[1,2,3,4,5,6,7,8,9,0,8,7,6,5,3]
i=0
final=[]
b=[]
count=0
while i<len(a):
    if count==3:
        final.append(b)
        b=[]
        count=1
    else:
        count+=1
    b.append(a[i])
        # count+=1
    i=i+1
print(final)