# Operator Overloading & Dunder Method(Special method).

class Employee:
    no_of_leaves = 8

    def __init__(self, argName, argSalary, argRole):
        self.name = argName
        self.salary = argSalary
        self.role = argRole
# argName,argSalary,argRole are the arguments and name,salary,role are the instance variable of the object.

    def print_details(self):
        return f"This is {self.name}, salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_no_of_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

# this dunder add method help us to do operator overloading.
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"This is {self.name}, salary is {self.salary} and role is {self.role}."

# methods starts and ends with __ is called dunder method
# __init__ is dunder init method.

emp1  = Employee("Harry", 345, "Programmer")
emp2 = Employee("Rohan", 65, "Cleaner")
print(emp1 + emp2)
print(emp1 / emp2)
# print(emp1)    # in this before repr dunder method --   <__main__.Employee object at 0x00000276B4F7EE70>  will get printed.
# after repr dunder method this can be modified and some understandable content can be displayed.
print(emp1)

# NOTE: __str__ dunder method is preferable over __repr__ dunder method, if both are present then on printing the object str method will
# get printed, unless until we consiously call the repr method.

# print(repr(emp1))