# Class Method as a Alternative Constructor.

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

    # Class Method as a Alternative Constructor.
# how good it be, if we can create a object just by passing a string (just passing a single argument - it creates a object).
#     let's define a function from_string that creates  object as we pass the string to it.
    @classmethod
    def from_string(cls, string):
    #     params = string.split("-")
    #     return cls(params[0], params[1], params[2])   # returns a object.
        # yha par cls - Employee class hai.

    # one liner
        return cls(*string.split("-"))   # returns a object.


vaibhav = Employee("Vaibhav Sharma", 569, "Web Developer")
rohan = Employee("Rohan Gupta", 1345, "App Developer")
sparsh = Employee.from_string("Sparsh-678-Java system design")
print(sparsh.role)
print(sparsh.no_of_leaves)

# list mai star(*) lga diya yeh(uskai elements) as an arguments pass ho jaigai function mai. - args concept.
