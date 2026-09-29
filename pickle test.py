import pickle

a_dict = {'a':11,2:[34,2,1]}
file = open('pickle_example.pickle','wb')
pickle.dump(a_dict,file)
file.close()

with open('pickle_example.pickle','rb') as file:
    a_dict1 = pickle.load(file)
print(a_dict1)