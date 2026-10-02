# Functions
# Two type of function --> user-defined and built-In

# 1).BUILT-IN function
# a). sum() function mai list ya tuple hona chaiye basically wo cheez jo iterable ho
# sum() function ka argument ek iterable cheez hona chaiyai - ex.., list, tupple etc
# syntax for other is sum(( ))

a = 9
b = 8
c = sum((a,b))  # press control key and click on sum -- will open all built-in functions in python
# c = sum([a,b])
# print(c)

# ( ) is called parenthesis


# 2). USER-DEFINED function
# jo user khud define karta hai

# SYNTAX
# we have to use - def and then write function name() and them enter the function by indentation

# def function1():
#     print("Hello you are in function 1")

# print(function1()) # return none
# function1()  # will only display the message
# function1()
# function1()

# function can also take input
# def function1(a,b):
#     print("Hello you are in function 1",a+b)
#
# # function1(5,7)
# function1(5,7)

# def function2(a,b):
#     average = (a+b)/2
#     print(average)
# function2(5,7)

# agar hum function ki value ko ek variable mai store karna chatai hai,how to do that

# def function2(a,b):
#     average = (a+b)/2
#     print(average)

# v = function2(5,7)
# print(v) # output is none which means that function nai chuch bhi nhi diya


def function2(a,b):
    average = (a+b)/2
    # print(average)
    return average

v = function2(5,7)  # v mai store ho jaigi return value
print(v)

# NOTE: pehlai program 59 line kai pass aaiga seedha yaani def ko ignore  karaiga and seedha variavle v kai pass aaiga and them code ko execute karna start karaiga and then read karnai
# kai baad function2 mai ghusaiga further things in function2 execute hogi and return value v mai aa jaigi


# DOCSTRING
# first string inside the function is called Docstring
def function2(a,b):
    """This is a function which will calculate average of two numbers
       this function doesn't work for three numbers"""  # This is DOCSTRING
    average = (a+b)/2
    return average

# v = function2(5,7)
# print(v)
# How to print DOCSTRING
print(function2.__doc__)