try:
    file = open('eeee','r+')
except Exception as e:
    print('there is no file named as eeee')
    response = input('do you want to craete a new file')
    if response == 'y':
        file = open('eeee','w')
    else:
        pass
else:
    file.write('ssss')
file.close()


