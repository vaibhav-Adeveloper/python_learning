# F strings and strings formatting

# strings formatting - to insert the variable between the string

# me = "vaibhav"
# a = "this is %s"%me
# print(a)

# Good way to do string formatting is
# by passing the tupple.

# me = "vaibahv"
# a1 = 3
# a = "this is %s %s"%(me, a1)  # we passed the tupple
# print(a)

# Another way of formatting is DOT FORMATTING

# me = "vaibhav"
# a1 = 3
# a = "this is {} {}"
# b = a.format(me, a1)
# print(b)

# me = "vaibhav"
# a1 = 3
# a = "this is {1} {0}"    # a1 will go in 1 and me will go in 0,   a.format(0, 1, 2, 3....)
# b = a.format(me, a1)
# print(b)


# Doing the formatting with the help of F-STRING #

# Best way to do formatting
# me = "vaibhav"
# a1 = 3
# a = f"this is {me} {a1}"
# print(a)

# me = "vaibhav"
# a1 = 3
# a = f"this is {me} {a1} {4*64}"
# print(a)

# WE CAN USE MODULE AND FUNCTION INSIDE THE F STRING
import math

me = "vaibhav"
a1 = 3
a = f"this is {me} {a1} {math.cos(65)}"
print(a)

# Whenever have to add many variable in a string use the F STRING
# ### instead using the + to add stirng use F string concept to add string
