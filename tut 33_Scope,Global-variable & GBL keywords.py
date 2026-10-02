# Scope, Global Variable,Global Keywords

l = 10  # Global variable, variable l have global scope, program mai jitnai bhi function hai wo saarai esai use kar saktai hai

# def function1(n):
#     print(l)
#     print(n, "I have printed")
#
# function1("This is me")
# print(l)  # Global variable l will be printed  (l = 10)


# def function1(n):
#     l = 5   # local variable, local scope, have scope only inside the function, outside the function l have value 10 store in it
#     m = 111  # local variable have scope only inside the function, outside the function m = 111 is nothing, means it is not thier
#     print(l)  # local variable l will be printed (l = 5)
#     print(n, "I have printed")
#
# function1("This is me")
# print(l)   # global variable l will be printed
# print(m)  # ERROR


# def function1(n):
#     # l = 5   # local variable
#     m = 111  # local variable have scope only inside the function, outside the function m = 111 is nothing, means it is not thier
#     print(l, m)  # local variable x and m will be printed  (l = 5 and m = 111)
#     print(n, "I have printed")
#
# function1("This is me")


# def function1(n):
#     # l = 5
#     m = 111  # local variable have scope only inside the function, outside the function m = 111 is nothing, means it is not thier
#     l = l + 45  # if we will try to change global variable but it's fail to do so
#     print(l, m)  # local variable x and m will be printed  (l = 5 and m = 111)
#     print(n, "I have printed")
#
# function1("This is me")


# def function1(n):
#     l = 5   # local variable, local scope, have scope only inside the function, outside the function l have value 10 store in it
#     m = 111  # local variable have scope only inside the function, outside the function m = 111 is nothing, means it is not thier
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# print(l)   # global variable l will be printed (l = 10)


# About Global Keyword
# if want to change the global variable inside the function then we have to use global keyword

# def function1(n):
#     # l = 5   # Local
#     m = 111
#     global l  # gives the permission to change the global variable
#     l = l + 45
#     print(l, m)   # global variable l (l=55) and local variable m (m=111) will be printed
#     print(n, "I have printed")
#
# function1("This is me")
# print(l)   # global variable l will be printed

# keyword - global - goes outside the function even if it is nested it goes outside of all function and then it find the variable.

# here - gobal x - will find the x variable here - reason.

# nested function means function inside function

# def vaibhav():
#     x = 20
#     def ishant():
#         global x  # why the value of variable x doesnt change - the reason is written above the function
#         x = 88
#     print("before calling ishant()", x)  # local variable x will be printed
#     ishant()
#     print("after calling ishant()", x)  # local variable x will be printed
#
# vaibhav()
#
# print(x) # global variable x wii be printed and rohan() func nai global variable x = 88 bna diya
# rohan() func nai bas yeh kaam kiya ki global variable x = 88 bna diya


x = 99  # global variable
def vaibhav():
    x = 20  # local variable
    def ishant():
        global x
        x = 88   # global variable x (x = 99) value changes to x = 88
    ishant()
    print("after calling ishant()", x)  # local variable x will be printed

vaibhav()

print(x)  # global variable x will be printed but remember that global variable x = 99 value changes to x = 88