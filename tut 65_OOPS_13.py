# Super() & overriding in classes.

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "special"

class B(A):
    # classvar2 = "I am in class B"
#   attribute override:
    classvar1 = "I am in class B"

#   constructor overwrite:
    def __init__(self):
        # super().__init__()    # in this case var1 and classvar1 value of class A will get overrided by class B.
        # self.var1 = "I am inside class B constructor"
        # self.classvar1 = "Instance var in class B"

        self.var1 = "I am inside class B constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()   # in this case var1 and classvar1 value of class B will get overrided by class A.
        print(super().classvar1)

#   jo cheez override jo jati hai wo run nhi hoti hai.
#   ab constuctor of class A will not run as it is overrrided by the class B, so only constructor of class B will run.

# agar mai chata hu ki super class ka bhi constuctor call ho jaai and subclass ka bhi, to call superclass constructor we have to
# use super().__init__

a = A()
b = B()
# constructor ek aisa method hai jo object bantai hi run ho jata hai.

print(b.classvar1)  # sabsai pehlai object - instance variable dundhai-gaa.

print(b.special)    # error - AttributeError: 'B' object has no attribute 'special'

print(b.var1, b.classvar1)

# sabsai pehlai instance variable ko dundhai gaa in class B and then in class A and then if it i not there then class variable ko dundhai-gaa
# in class B and then in class A.  --> overriding.
