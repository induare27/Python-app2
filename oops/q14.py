#Q14: Create a Person class with private variable __age. Add validation using getter-setter.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=0
        self.setter(age)      #for validation
    def getter(self):
        return self.__age
    def setter(self,age):
        if 0<=age<=120:
            self.__age=age
        else:
            print("Invalid age")
    def display(self):
        print(f"Name:{self.name}; Age:{self.__age}")
p=Person("Priya",23)
p.display()
p.setter(130)
p.setter(21)
print("Updated age:",p.getter())
    