# jab function banatai hai in class ,toh self aa jata hai - matlb hum iss function mai sirf object as an arguments dai saktai hai
# isskai alawa koi dusra argument nhi dai paigai.

# lekin agar hum chahatai hai ki object kai alawa bhi arguments dai sakai in the function made in class, then we have to make the
# class methods in the class, to pass multiple arguments.

# Static method in python.

# koi aisa function banana hai ki jo na hi self or class ko as an argument lai, balki apna koi kaam karai as an independent function.

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


vaibhav = Employee("Vaibhav Sharma", 569, "Web Developer")
rohan = Employee("Rohan Gupta", 1345, "App Developer")

iron_man = Employee.from_string("Iron_Man-1/0-AI developer")
iron_man.print_message("I am back as a Devil.")
Employee.print_message("I am Dr. DOOM")

# static method ko hum, instance of class and class dono sai access kar saktai hai.
    