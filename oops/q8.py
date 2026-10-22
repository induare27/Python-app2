#Q8. Create a class Vehicle with a method start(). Inherit a class Car from it with a method drive(). Show single inheritance.

class Vehicle:
    def start(self,mode):
        self.mode=mode
        print("vehicle mode:",self.mode)
class Car(Vehicle):
    def drive(self,speed):
        self.speed=speed
        print("car speed:",self.speed)
c=Car()
c.start("road")
c.drive("100km per 1hr")

