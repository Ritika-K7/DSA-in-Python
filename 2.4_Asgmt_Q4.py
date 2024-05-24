'''Define a class Book with instance object variables bookid,title,price. Initialise them 
via __init__() method . Also define method to show book variable '''

class Book:
    def __init__(self,bookid=None,title=None,price=None):
        self.bookid=bookid
        self.title=title
        self.price=price
    def setBookid(self,bookid):
        self.bookid=bookid
    def setTitle(self,title):
        self.title=title
    def setPrice(self,price):
        self.price=price
    def show(self):
        print(self.bookid,self.title,self.price)    

b1=Book(101,'The breadcrumbs',120)     
b1.show()