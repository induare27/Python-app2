#Q12: Abstract Shape Class

from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(Self):
        pass
class circle(shape):
    def area(self,radius):
        self.radius=radius
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
c=circle()
print(c.area(5))
print(c.perimeter())
