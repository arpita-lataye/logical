sentence = 'This is a sentence'
word=""
for w in sentence :
    if w.isalpha():
        word=word+w

    elif not w.isalpha():
      print(word)
      word=""
print(word)


# a='tiamo suga sarangio hansimida'
# n=''
# for i in a:
#     if i.isalpha():
#         n=n+i

#     elif not i.isalpha():
#         print(n)
#         n=''
# print(n)