# Object Introspection.
# it means kisi bhi object kai baarai mai janna, uski information laina.

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set, please set it using setter"
        return f"{self.fname}.{self.lname}@nitsri.ac.in"

    @email.setter
    def email(self, string):
        print("Setting Now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

Skillf = Employee("Skill", "F")
print(Skillf.email)

# Object Introspection.

print(type(Skillf))
print(type("hello i am a string"))

print(id(Skillf))
print(id("hello i am a string"))

o = "I am a String"
print(dir(o))

print(dir(Skillf))
# dir function, wo saarai methods display karta hai jo hum uss object pai perform kar saktai hai, jo uss obj kai liyai define hai.


import inspect
print(inspect.getmembers(Skillf))   # saarai kai saarai attribute btaigaa.

# Exercise :- use of inspect module.
# beautifully present but seperately, all the class varibales, instance varibales, attributes, methods etc.
