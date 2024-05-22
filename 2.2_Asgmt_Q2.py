'''Define a class Circle with instance object variable radius.Provide setter and 
getter for radius .Also define getArea() and getCircumference() mathod'''

class Circle:
    def __init__(self,radius=None):
        self.radius=radius

    def setRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius

    def getArea(self):
        return(3.14*self.radius*self.radius)
    def getCircumference(self):
        return(2*3.14*self.radius)


c1=Circle(3)
print(c1.getArea())
print(c1.getCircumference())