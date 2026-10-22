'''Q4. Create a class Employee with:
Class variable company_name = "Infosys"
Instance variables: name and salary
Create 2 objects and modify the company name using the class'''

class Employee:
    company_name="Infosys"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

Employee.company_name="tcs"
e1=Employee("Priya",40000)
e2=Employee("indu",60000)
print(e1.__dict__)
print(e1.company_name)