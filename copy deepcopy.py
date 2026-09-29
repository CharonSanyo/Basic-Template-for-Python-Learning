import copy
a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))
c = copy.copy(a)
print(id(a) == id(c))
a = [1,2,[3,4]]
d = copy.copy(a)
print(id(a)==id(d))
print(id(a[2])==id(d[2]))
e = copy.deepcopy(a)
print((e[2])==id(a[2]))