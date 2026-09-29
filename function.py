def function():
    print('This is a function')
    a = 1+2
    print(a)

function()

def fun(a,b):
    c = a*b
    print('c is',c)

fun(1,5)
fun(a=2,b=5)

def sale_watermelon(p,c='red',b='haoge',s='Ture'):
# 默认值统一放到后面
    print('p:',p,
          'c:',c,
          'b:',c,
          's:',s)

sale_watermelon(2,'red','haoge','Ture')
sale_watermelon(2)
sale_watermelon(2,c='blue')
