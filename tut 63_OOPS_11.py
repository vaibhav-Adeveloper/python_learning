# Public, Protected, and Private Access Specifiers.

# remember the concept with the House Analogy.
# A paper with some information to be shared with ... so stcik it to...
# Public - to make information available to everyone, stick it outside the house, so anyone crossing it can see it.
# Protected - to make information available to our family members only,stick it inside the house, so any family member crossing can see.
# Private - to make information available to only me, stick it inside my room.

# Naming Convention.
class Employee:
#   below three variables are Public.
    no_of_leaves = 8
    var = 8
    nar = 1

#   To make Protected variables, just start the variable with underScore _
    _protect = 84

#   To make Private variables, just start the variable with double underScore __
    __private = 1

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

emp = Employee("mahesh", 564, "Market Research")
print(emp._protect)

# print(emp.__private)     # error will occur
# python have done name mangling.

# how to access private variable :-
print(emp._Employee__private)  # this is called name mangling.

# name mangling is the process of complexing the private variable, so it can not be used easily and anywhere.
# name mangling --> converts/will save   __private into/as _Employee__private


# Meaning of Protected variable in OOPS:
# sirf base class and wo wali saari classes jo iss base class sai derive ho rhi hai, wo sirf issai use kar sakti hai.

# Meaning of Private variable in OOPS:
# sirf base class hi usko access kar sakti hai.