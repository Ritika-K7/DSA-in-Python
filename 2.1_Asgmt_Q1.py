'''Define a class Person with instance object variable name and age.
Set instance oject variable in  __init__()method.Also define show() methoda to display name and age of a person.'''
class Person:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def setName(self,name):
      self.name=name   
    def setAge(self,age):
       self.age=age
    def getName(self):
       return self.name
    def getAge(self):
       return self.age   
    def show(self):
       print(self.name,self.age)

p1=Person("Rahul",36)
p1.show()
