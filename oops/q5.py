'''Q5. Create a class Laptop with:
Class variable: total_laptops = 0
Inside __init__, increment total_laptops every time an object is created
Show how class variables can be used for counting instances'''

class Laptop:
    total_laptops=0
    def __init__(self):
        Laptop.total_laptops+=1
l1=Laptop()
print(Laptop.total_laptops)