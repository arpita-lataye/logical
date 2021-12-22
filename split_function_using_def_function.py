def my_split(s, sep=' '):
    s = s.lstrip(sep)
    if sep in s:
        pos = s.index(sep)
        found = s[:pos]
        remainder = my_split(s[pos+1:])
        remainder.insert(0, found)
        return remainder
    else:
        return [s]

print (my_split("This is a sentence"))


# sentence = 'This is a sentence'
# word=""
# for w in sentence :
#     if w.isalpha():
#         word=word+w

#     elif not w.isalpha():
#       print(word)
#       word=""
# print(word)

# my_str='This is a sentence'
# split_value = []
# tmp = ''
# for i in my_str+' ':
#     if i == ' ':
#         split_value.append(tmp)
#         tmp = ''
#     else:
#         tmp += i   
# print(split_value)