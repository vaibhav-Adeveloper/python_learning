# Creating our first Class
# Why we make CLASS
# repeatibility ko kaam karta hai - class bna kai
# code ko bahot zyada organise kartai hai - class bna kai

# object are the instance of the class.

class student:
    pass

vaibhav = student()  # Object-1 of class student
ishant = student()  # Object-2 of class student.
# Both vaibhav and ishant object are Different.
print(vaibhav,ishant)  # gives memory location of these object.

# Creating the Instance Variable of the Object.
vaibhav.name = "Vaibhav"
vaibhav.std = 12
vaibhav.section = "A"
ishant.name = "Ishant"
ishant.subjects = ["Hindi","Physics","Maths"]

print(vaibhav.name, ishant.name)
print(vaibhav.std)
print(vaibhav.section, ishant.subjects)