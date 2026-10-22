#Q10. Use super() to call the constructor of Employee class from Manager class.

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name,salary)
        self.department=department

m=Manager("Priya",60000,"Marketing")
print(m.name,m.salary,m.department)
