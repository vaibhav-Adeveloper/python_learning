# self and __init__() (CONSTRUCTOR).

# class Employee:
#     no_of_leaves = 8
#     def print_details(self):
#         return f"This is {self.name}, salary is {self.salary} and role is {self.role}."
#
# # self means wo object jispai, yeh function lgaya jaa rha hai.
# # self ka matlb hai wo object, jispai yeh function lgaigaa.
#
# vaibhav = Employee()
# rohan = Employee()
#
# vaibhav.name = "Vaibhav Sharma"
# vaibhav.salary = 500
# vaibhav.role = "Web Developer"
#
# rohan.name = "Rohan Gupta"
# rohan.salary = 600
# rohan.role = "App Developer"
#
# print(rohan.print_details())  # iss function mai automatically, as an argument rohan chala jaiga.

# constructor :-
# Employee class ko arguments dainai kai liyai, humai constructor banana padta hai.
# vaibhav = Employee("Vaibhav Sharma", 500, "Web Developer")   # just give arguments to class and it will create the object with the following instance variables.
# to do this we have to make constructor.

# to make constructor we have to make a init() function.

class Employee:
    no_of_leaves = 8
    def __init__(self,argName,argSalary,argRole):
        self.name = argName
        self.salary = argSalary
        self.role = argRole
# argName,argSalary,argRole are the arguments and name,salary,role are the instance variable of the object.
    def print_details(self):
        return f"This is {self.name}, salary is {self.salary} and role is {self.role}."

vaibhav = Employee("Vaibhav Sharma", 569, "Web Developer")
# this will create the vaibhav name object and its instance variables name,salary,role.

print(vaibhav.role)
print(vaibhav.__dict__)
