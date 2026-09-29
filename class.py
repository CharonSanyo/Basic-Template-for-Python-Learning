class Calculator:
    name = 'NB calculator'
    price = 18
    #固有属性
    def __init__(self,name,price,hight,width,weight):
        self.n = name
        self.p = price
        self.h = hight
        self.wid = width
        self.wei = weight
        #自己输入的属性
    def add(self,x,y):
    #    print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

#calcul = Calculator()
#print(calcul.name)
#add = calcul.add(10,11)
#minus = calcul.minus(10,11)

c = Calculator('NB',1,2,3,4)
print(c.name)