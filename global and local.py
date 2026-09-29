X=100

def fun():
    a = 10
    a = X
    print(a)
    return a+100

print(fun())
print(X)


a = None
def fun():
    global a
    a = 10
    print(a)
    return a+100

print('a past=',a)
print(fun())
print('a now=',a)