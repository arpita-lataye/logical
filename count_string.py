a=input('enter number:')
p=[]
k=[]
count=0
count1=0
i=0
while i<len(a):
    if a[i]>='a' and a[i]<='z' or a[i]>='A' and a[i]<='Z':
        p.append(a[i])
        count+=1
    else:
        k.append(a[i])
        count1+=1
    i+=1
print(count,p)
print(count1,k)

# string1=input('enter string:')
# l1=[]
# l2=[]
# count=0
# count1=0
# letter1='asdfghjklmnbvcxzqwertyuiop'
# letter2='ASDFGHJKLMNBVCXZQWERTYUIOP'
# for i in range(len(string1)):
#     if string1[i] in letter1 or string1[i] in letter2:
#         l1.append(string1[i])
#         count+=1
#     else:
#         l2.append(string1[i])
#         count1+=1
# print(l1)
# print(l2)
# print(count)
# print(count1)
