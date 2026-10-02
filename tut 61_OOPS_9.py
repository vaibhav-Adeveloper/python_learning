# Multiple Inheritance.

class Employee:
    no_of_leaves = 8
    var = 8
    nar = 1

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

class Player:
    no_of_games = 4
    var = 9
    nar = 2

    def __init__(self,name,games):
        self.name = name
        self.game = games

    def print_detPly(self):
        return f"This is {self.name}, plays {self.salary}."

class CoolProgramer(Employee, Player):  # 'order' is important.
    language = "Goo"
    var = 10
    def printLanguage(self):
        print(self.language)


vaibhav = Employee("Vaibhav Sharma", 569, "Web Developer")
rohan = Employee("Rohan Gupta", 1345, "App Developer")

yesh = Player("Yesh", ["Cricket", "Badminton"])

nauroz = CoolProgramer("Nauroz", "8978", "CoolProgrammer")
# print(nauroz.print_details())
# nauroz.printLanguage()

print(nauroz.var)
print(nauroz.nar)


# sabsai pehlai wo khud mai dhundaigaa.
# koi bhi class variable, methods of super class hogaa, sabse pehlai ussai Employee class mai dhundaiga ,iskai baad agar nhi mila toh
# next super class Player mai. "Order is important"