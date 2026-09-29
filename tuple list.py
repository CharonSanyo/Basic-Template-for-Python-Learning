a_tuple = (1,2,3,4,5)
another = 2,3,4,1,2
a_list = [1,2,3,5,4]#索引从0开始

for content in a_list:
    print(content)

for content in a_tuple:
    print(content)

for index in range(len(a_list)):
    print('index='.index,'number in list=',a_list[index])

#list
a = [1,2,3,4,3,2]
a.append(0)
a.insert(1,0)
a.remove(2)
print(a)
print(a[0])
print(a[-1])
print(a[0:3])
print(a[:3])
print(a[5:])
print(a.index(2))
print(a.count(3))
a.sort()
a.sort(reverse=True)
print(a)
