# Setters and Property Decorators.

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@nitsri.ac.in"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    # def email(self):
    #     return f"{self.fname}.{self.lname}@nitsri.ac.in"

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


ishant = Employee("Ishant", "Sharma")
priyanshu = Employee("Priyanshu", "Verma")

print(ishant.explain())
print(priyanshu.explain())
# print(priyanshu.email)
#
# priyanshu.fname = "The Great"
# print(priyanshu.email)
# priyanshu object ka first name change nhi hoga -->
# reason - jab object creation hua tha line 35, ussi time pai constructor run hua tha and ussnai email ko initialise kar diya tha with the first name Priyanshu.

# isi problem ko solve karta hai setter.
# print(priyanshu.email())
# priyanshu.fname = "The Great"
# print(priyanshu.email())
# ab change ho jaiga fname.

# but we have to maintain encapsulation in the class, that is to hide the class methods implementation.
# i want to give email as an attribute (obj.email) not as an function email() (obj.email()).
# we can achieve this using property decorators.

# after using property decorator.
# we don't have to call the function, we can use it as a attribute.
print(priyanshu.email)
priyanshu.fname = "The Great"
print(priyanshu.email)

# setter concept.
# want to give the attribute email value manully
# and by giving the value of attribute email - the fname and lname get changes correspondly.
priyanshu.email = "hello.Bye@nitsri.ac.in"    # AttributeError: cant set attribute.
# so to able to do above stuff (to modify attribute), we create setter.

print(priyanshu.fname)
print(priyanshu.lname)
print(priyanshu.email)

# if we want to delete email attribute, we have to make a deleter.

del priyanshu.email
print(priyanshu.email)


"""
SUMMARY:

@property
1). agar chahtai ho ki mai object ka fname and lname dunga and issai object ka email change ho jaae.
2). and aslo have to use email() function as an attribute email with the object.

@setter
1). agar chahtai ho ki object kai attribute email ki value dunga  obj.email = ".." and issai obj ka fname and lname change ho jaae.
"""