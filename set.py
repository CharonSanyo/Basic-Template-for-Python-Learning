char_list = ['a','b','c','c']
print(set(char_list))
print(type(set(char_list)))
print(type(set(char_list)))
sentence = 'haoge sharenle'
print(set(sentence))
unique_char = set(char_list)
unique_char.add('x')
#unique_char.clear()
print(unique_char)
print(unique_char.remove('x'))
print(unique_char.discard('y'))
print(unique_char)

set1 = unique_char
set2 = {'a','e','i'}
print(set1.difference(set2))
print(set1.intersection(set2))
