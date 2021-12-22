# here we multiple two digit value without using multiple operator.
a=int(input('enter a number:'))
b=int(input('enter a number:'))
c=a/(1/b)   #a/1b=>(a/1)/(1/b)=>a/1*b/1=>a*b/1=>a*b
# print('the multiple value of',a,'and' ,b, 'is:',c)
d=int(c)  #here we get output in float ,so we convert it into integer value.
print('the multiple value of',a,'and' ,b, 'is:',d)