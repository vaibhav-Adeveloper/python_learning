# Anonymous/Lambda function in python
# it is a one liner function

# adding two number function

# def add(a,b):
#     return a+b
#
# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# print("Sum of two number is:",add(a,b))


# forming above function using the lambda function

# adding = lambda a,b: a+b
#
# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# print("Sum of two number is:",adding(a,b))


# basically
#      def add(a,b):
#          return a+b
#         OR
#     adding = lambda a,b: a+b

# Are Same Things

# How to use lambda function in sort function

def a_first(a):
    return a[1]   # a[index]  # yeh function kya return kar rha hai, jo bhi iskai andar jaa rhai hai uski pehli index return kar rha hai.

# a = [[1,9], [13,5], [7,8]]   # We formed List of List
# a.sort(key=a_first)
# key ek argument hota hai jo Function ko as a input laita hai.
# print(a)

# iss a_first function ko hum lambda function kai sath replace kar saktai hai.

a = [[1,9], [13,5], [7,8]]
a.sort(key=lambda x : x[1])
print(a)


a = lambda x : x*x  # means ek aisa function bna do, agar jisko x doo toh wo x square return kar dega