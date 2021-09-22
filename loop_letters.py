# print all letters except "e" and "s"
i=0
a='geeks for geeks'
while i< len(a):
    if a[i]=='e' or a[i]=='s':
        i=i+1
        continue
    print('current letter:', a[i])
    i=i+1