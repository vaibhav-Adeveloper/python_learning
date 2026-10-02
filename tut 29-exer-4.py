# Exercise-4
# Pattern Print
# Question - input is a integer n and print the below pattern
# take boolean variable and have to take input 1 or 0 and if that boolean vaiable is True and print pattern below that and if boolean vaiable is False and print pattern below that
# n is no of rows
# True n = 4 here
# *
# **
# ***
# ****
#
# False
# ****
# ***
# **
# *


# TypeCasting
# n = 0
# m = bool(n)
# print(m)

# print(bool(n))


n = int(input("Enter the number of rows: "))
print("\nEnter 0 for false or 1 for true")
m = int(input("Enter the number: "))

if bool(m)==True:
    for i in range(n):
        for j in range(n):
            if (j <= i):
                print("*", end="")
        print()
else:
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        print()