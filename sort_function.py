a=[1,5,4,7,8,3,6,9]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            c=a[j]
            a[j]=a[j+1]
            a[j+1]=c
        
print(a)


# for i in range(len(a)-1,0,-1):
#     for j in range(i):
#         if a[j]>a[j+1]:
#             c=a[j]
#             a[j]=a[j+1]
#             a[j+1]=c
# print(a)

def fun(a):
    # a=[1,5,4,7,8,3,6,9]
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                c=a[j]
                a[j]=a[j+1]
                a[j+1]=c
    return(a)
b=[14,67,43,200,3,56,78,98,102,234]      
print(fun(b))