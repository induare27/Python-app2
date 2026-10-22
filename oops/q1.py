#Q1. Create a class Car with brand, model, and year. Create two objects and print their details.
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print(f"The Brand of car is {self.brand}")
        print(f"The model of car is {self.model}")
        print(f"The year of car is {self.year}")
        print("--------------------------------")
c1=Car("BMW","5th version",2020)
c2=Car("Audi","latest version",2025)
c1.display()
c2.display()
