#Q3. Create a class Book with attributes title, author, and pages. Add a method is_long_book() that returns True if pages > 300.
class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def is_long_book(self):
        if self.pages>300:
            print("True")
        print("False") 
b1=Book("Twisted","Ana haung",200)
b1.is_long_book()        