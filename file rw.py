text = 'This is my first test.\nThis is next line.\nThis is last line.'
print(text)

my_file = open('my file.txt','w')
my_file.write(text)
my_file.close()
#r read w write


append_text = '\nThis is appended file.'

my_file = open('my file.txt','a')
my_file.write(append_text)
my_file.close()

file = open('my file.txt','r')
content = file.read()
content = file.readline()
second_read_time = file.readlines()
python_list = [1,2,3,4,5,'dfdf','dfdf']
print(content)


