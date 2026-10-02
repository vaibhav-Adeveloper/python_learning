# Single Inheritance.

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

    @classmethod
    def from_string(cls, string):
        return cls(*string.split("-"))   # returns a object.

    @staticmethod
    def print_message(str):
        print(f"This is the message sent by iron man : {str}")


class Programmer(Employee):

    no_of_holidays = 70

    def __init__(self, argName, argSalary, argRole, argLanguage):
    #     Use SUPER keyword instead of writing below code.
        self.name = argName
        self.salary = argSalary
        self.role = argRole
        self.language = argLanguage

    def printProg(self):
        return f"The Programmer's name is {self.name}, salary is {self.salary} and role is {self.role} and know the languages: {self.language}."


vaibhav = Employee("Vaibhav Sharma", 569, "Web Developer")
rohan = Employee("Rohan Gupta", 1345, "App Developer")

# praful = Programmer("praful", 1500, "Software Developer")
# sparsh = Programmer("sparsh", 1400, "DevOps Developer")

praful = Programmer("praful", 1500, "Software Developer", ["Java", "JavaScript"])
sparsh = Programmer("sparsh", 1400, "DevOps Developer", ["Java", "Cpp"])

print(praful.printProg())   # Programmer class method.
print(praful.print_details())   # Employee class method.
print(sparsh.no_of_holidays)