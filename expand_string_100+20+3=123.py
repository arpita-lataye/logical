string=input('enter number:')
b=''
i=0
while i<len(string):
    b+=string[i]
    # print(b)
    j=1
    while j<=len(string)-(i+1):
        b+="0"
        j=j+1
    if i==(len(string)-1):
        break
    else:
        b+='+'
    i=i+1
print(b)


