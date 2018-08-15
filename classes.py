#!/c/Python27/python

# class definition

class Rectangle:
    def __init__(self,name,a,b):
        self.name = name
        self.a = a
        self.b = b

    def parameter(self):
        return self.a*2+self.b*2

    def area(self):
        return self.a*self.b

#Instances

r1 = Rectangle('Kitchen',2,4)
r2 = Rectangle('hall',1,3)

for r in [r1,r2]:
    print ("{} sides: {},{}".format(r.name,r.a,r.b))
    print("{} parameter: {}".format(r.name,r.parameter()))
    print ("{} area: {}".format(r.name,r.area()))
