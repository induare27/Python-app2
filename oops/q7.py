'''Q7. Create a class Student where:
Marks are private
Use getter and setter with validation
Try setting negative marks and print the result'''


class Student:
    def __init__(self):
        self.__marks=0
    def get_marks(self):
        return self.__marks
    def set_marks(self,m):
        if m>0 and m<=100:
            self.__marks+=m
        else:
            print("Invalid marks")
s1=Student()
s1.set_marks(85)
s1.set_marks(-23)
print(s1.get_marks())

