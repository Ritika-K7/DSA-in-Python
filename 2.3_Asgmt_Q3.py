'''Define a class Rectangle with length and breadth as instance object variable .
Provide setDimensions(), showDimension() and getArea() method in it'''

class Rectangle:
    def __init__(self,length=None,breadth=None):
        self.length=length
        self.breadth=breadth
    
    def showDimensions(self):
            print(self.length,self.breadth)  

    def setDimensions(self,length,breadth):
            self.length=length
            self.breadth=breadth

    def getArea(self):
            return self.length*self.breadth
      
r1=Rectangle(2,6)
r1.showDimensions()
print(r1.getArea())            