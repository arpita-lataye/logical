a=[1,4,8]
for i in a:
    for j in range(1,9,1):
        if j not in a:
            a.append(j)
# print(a)
# a.sort()
print(a)
# a=[1,4,8,2,3,5,6,7]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            c=a[j]
            a[j]=a[j+1]
            a[j+1]=c
print(a)


# a=[1,4,8]
# for i in a:
#     for j in range(1,9,1):
#         if j not in a:
#             a.append(j)
# # print(a)
# # a.sort()
# print(a)
# # a=[1,4,8,2,3,5,6,7]
# for i in range(len(a)-1,0,-1):
#     for j in range(i):
#         if a[j]>a[j+1]:
#             c=a[j]
#             a[j]=a[j+1]
#             a[j+1]=c
        
# print(a)