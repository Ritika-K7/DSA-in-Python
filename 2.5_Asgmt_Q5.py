'''Define a class Team with instance oject variable a list of team member names.
Provide methods to input member names and display member number '''
class Team:
    def __init__(self,name=[None]):
        self.name=name

    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name

    def show(self):
        print(self.name)
            
t1=Team(['Rahul','chavi','sai'])
t1.show()