# RECURSION
# RECURSION in function
# RECURSION - ka matlab hota hai function kai andar function ko use karna

# def print2(str1):
#     print("This is",str1)
#     print("This is " + str1)

# print2("vaibhav")


# Recursion
# def print2(str1):
#     print2(str1)  # function ko function kai andar call karna but we have haven't break the calling so function kai andar yeh ghusta jaiga,ghusta jaiga
#     print("This is",str1)
#
# print2("vaibhav")


# lets build the function calculating the factorial with the help of ITERATIVE approach
# n! = n * n-1 * n-2 ......1
# n!  = n * (n-1)!


# def factorial_iterative(n):
#     """
#     this function takes the input/arguments n and return n factorial(n!)
#     :param n: Integer
#     :return: n * n-1 * n-2 ..........1
#     """
#     fac = 1
#     for i in range(n):  # i value starts from ZERO
#         fac = fac * (i+1)
#     return fac
#
# number = int(input("Enter the Number:"))
# print(factorial_iterative(number))


# lets understand the recursion with the help of example
# lets calculate the factorial with the help of RECURSIVE technique/approach

# def factorail_recursion(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorail_recursion(n-1)
# # Recursion Working
# # In recursion stack.
# # 5 * factorail_recursion(4)
# # 5 * 4 * factorail_recursion(3)
# # 5 * 4 * 3 * factorail_recursion(2)
# # 5 * 4 * 3 * 2 * factorail_recursion(1)
# # 5 * 4 * 3 * 2 * 1 = 120
#

def factorail_recursion(n):
    return 1 if n == 1 or n == 0 else n * factorail_recursion(n - 1)


number = int(input("Enter the Number:"))
# print(factorail_recursion(number))


# QUIZ
# print the fibonacci series upto nth fibo. terms.
# 0 1 1 2 3 5 8 13 21 34 .....
# fibonacci series starts from 0 1 and further series number comes from adding the previous two numbers

# def fibo_series_iterativeMethod(n):
#     if n == 0:
#         return
#     elif n == 1:
#         return 0
#     else:
#         a = 0
#         b = 1
#         c = 0
#         print(a, b, end = " ")
#         for i in range(n-2):  # i values start from ZERO
#             c = a + b
#             a = b
#             b = c
#             print(c, end = " ")
#
# terms = int(input("Enter the term upto which fibonacci series to be printed:"))
# print(fibo_series_iterativeMethod(terms))

print("Enter the number of terms:", end=" ")
n = int(input())
a = 0
b = 1
def fibo_recur(m):
    if m<1:
        return
    global a
    global b
    print(str(a) + " ", end="")
    sum = a + b
    a = b
    b = sum
    fibo_recur(m-1)

fibo_recur(n)


# QUIZ
# WAP to find the 'terms' of fibonacci series

def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

term = int(input("\nEnter the term:"))
print(fibonacci_recursive(term))