# Abstract base class and @abstractmethod(it is decorator).

# ek kaam kartai hai Shape naam ki base class banatai hai, jo kuch rules ko strictly implement karaigii in all classes,
# jaisai sabhi classes kai pass printarea function jarrur ho.
# aisai order kai saath classes bananai kai liyai hum 'abc meta class' ka istamal kartai hai.

# from abc import ABCMeta, abstractmethod
# OR
from abc import ABC, abstractmethod


# class Shape(metaclass=ABCMeta):
#     OR
class Shape(ABC):
# sabko printarea naam ka method implement karna hai.
# abstract method means yeh sab kai liyai define karna hai.

    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

# rect1 = Rectangle()     # will throw a error - TypeError: Can't instantiate abstract class Rectangle without an implementation for abstract method 'printarea'
# agar app shape class mai metaclass=ABCMeta likhtai ho, toh isskai baad agar app rectangle class mai printarea naam ka method nhi banaogai
# toh error aa jaiga.

rect1 = Rectangle()


# agar app Shape class sai inherit kar rhai hai kisi class ko toh app kai liyai yeh jaruri hai ki app printarea method ko define karai apnai andar (uss subclass kai andar).


# NOTE: app abstract base class kai objects nhi bana saktai hai.
# obj1 = Shape()    # error