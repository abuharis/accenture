#!/c/Python27/python

# class definition

class Rectangle:
    def __init__(self,name,a,b):
        self.__name = name
        self.a = a
        self.b = b

    def parameter(self):
        return self.a*2+self.b*2

    def area(self):
        return self.a*self.b

    def getName(self):
        return self__name
#Instances

r1 = Rectangle('Kitchen',2,4)
r2 = Rectangle('hall',1,3)

for r in [r1,r2]:
    print ("{} sides: {},{}".format(r.getName,r.a,r.b))
    print("{} parameter: {}".format(r.getName,r.parameter()))
    print ("{} area: {}".format(r.getName,r.area()))
