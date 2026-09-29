a = True
while a:
    b = input('type something')
    if b == '1':
        a = False
    else:
        pass

print('finish run')

# break continue

while True:
    b = input('type something')
    if b == '1':
        break
    else:
        pass
    print('still in while')

print('finish run')

while True:
    b = input('type something')
    if b == '1':
        continue
    else:
        pass
    print('still in while')

print('finish run')