# All about variables
# Variables is just like a container.
print("Lets get started")

var1 = "Hello World"  # String variable
var2 = 4    # integer variable
var3 = 36.7  # floating point variable/float variable--> (can take decimal value)
var4 = " vaibhav"
var5 = " 32"  #  its a string
var6 = "44"  #  its a string
var7 = "34"  #  its a string
print(var1)
# about--> type function
print(type(var1))
print(type(var2))
print(type(var3))
print()
print(var2 + var3)
#print(var1 + var3)  # Error will occur,we are adding string with number
print(var1 + var4)
print(var1 + var5)
print(var6 + var7)  # CONCATENATION of two string has occured-->Two string get ADDED
print()

""" CONCEPT OF TYPE-CASTING 
it means converting type of one variable into another type
"""
"""
 type-casting function are:
 str()
 int()
 float()
 """
print(int(var6) + int(var7))
print(1000 * int(var6) + int(var7))
print(str(var2) + str(var3))

# To print a string many Times
print(10 * "Hello World")
print(10 * "Hello World \n")
# To print a number many Times
# first we type-cast a number into a string.
print(10 * str(int(var6) + int(var7)))
print()
"""
Quiz
Exercise
Project
"""

""" # how to take a input from a user
# we have to use input function,below is how we take a input from user
# variable name = input()

### IMPORTANT THING TO NOTE ###:
###*** jo bhi aap number input karaigai wo as a STRING uss variable mai store hoo jaigaa.
"""
print("Enter the number")
num = input()
# remember num is a string
print("Entered number is:", num)
# print("Entered number is:", num + 10)   # ERROR --> string + number -->INVALID thing
print("Adding ten to Entered number:", int(num) + 10)
print()

"""Quiz = make a calculator that add two number"""
print("Enter the First Number:",end=" ")
num1 = input()
print("Enter the Second Number:",end=" ")
num2 = input()
# remember num1 and num2 is a string variable
# print("Sum of Two Number is:",num1 + num2)   # WRONG --> two string will get concatenated.
print("Sum of Two Numbers is:",int(num1) + int(num2))
print()

""" DATA TYPE
1.integer
2.string
3.float 
4.boolean """


