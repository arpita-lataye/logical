n=int(input('enter the number:'))
x = n // 2
y = []
while x * x != n:
        x = (x + (n // x)) // 2
        y.append(x)
if x in y:
    print("perfect square")
else:
    print("not a perfect square")


# n=int(input("enter the number:"))
# i=0
# while i>n:
#     j=1
#     while j<i:
#         if j*j==i:
#             print(i,"is a perfect square")
#             break
#         j=j+1
#     i+=1