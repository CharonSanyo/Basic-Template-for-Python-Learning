import re
# matching string

pat1 = 'cat'
pat2 = 'bird'
string = 'dog runs to cat'
print(pat1 in string)
print(pat2 in string)

print(re.search(pat1 in string))
print(re.search(pat2 in string))
