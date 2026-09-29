a_list = [1,2,3,4,5,3,4]
d = {'a':[1,2],'p':{1:3,3:'a'},'0':3}
d2 = {1:'a','c':'b'}
print(d['a'])
print(a_list[0])

del d['p']
print(d)
d['b'] = 20
print(d)#字典没有顺序

print(d['pear'][3])
