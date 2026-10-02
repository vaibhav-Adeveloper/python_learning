# Class Methods.

class Employee:
    no_of_leaves = 8

    def __init__(self, argName, argSalary, argRole):
        self.name = argName
        self.salary = argSalary
        self.role = argRole
# argName,argSalary,argRole are the arguments and name,salary,role are the instance variable of the object.

    def print_details(self):
        return f"This is {self.name}, salary is {self.salary} and role is {self.role}."

#   To make claas method, we have to use class method decorators.
    @classmethod
    def change_no_of_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


vaibhav = Employee("Vaibhav Sharma", 569, "Web Developer")
rohan = Employee("Rohan Gupta", 1345, "App Developer")

print(vaibhav.no_of_leaves)
# vaibhav.no_of_leaves=10  # this will create a new instance variable of the object vaibhav.
# print(vaibhav.no_of_leaves)  # pehlai yeh instance variable check karaigaa and if not found then go to find class variable.
print(vaibhav.__dict__)


# agar hum chahtai hai ki function kai through no_of leaves_ ko change karna, for this we have class methods.
vaibhav.change_no_of_leaves(23)   # this will change the class variable.
print(vaibhav.no_of_leaves)
# print(rohan.no_of_leaves)

# vaibhav kisi na kisi class ka object hoga, toh wo class jaiga in the 'cls' of class method.
# uss object ki class jaigi in the cls of class method.

# on changing vaibhav no_of_leaves through class method, rohan no_of_leaves also get changed.
# class method - class variables ko change karta hai, class kai attributes ko change karta hai.

# cls ? - cls hai wo class, jiska instance hai wo wla object (vaibhav) jispar yeh function run kar rha hai change_no_of_leaves().