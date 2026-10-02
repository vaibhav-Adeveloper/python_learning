# Raise keyword in python.

# how we can raise our own exception.

# About raise keyword.

a = input("What is your name: ")
b = input("How much do you earn: ")

if int(b) == 0:
    raise ZeroDivisionError("Earning Zero, get out from here.")

if a.isnumeric():
    raise Exception("Numbers input is not allowed.")
#
# print(f"Hello {a}")

# 1000 lines of code taking 1 hour.
"""
//  code task  //
"""

# concept:
# agar a numeric input hua toh hum aisa nhi karaigai ki code ko run honai degai, jabki a wrong input aaya hai (numeric),
# aisa nhi ki wrong input aaya and phir bhi hum 1 hour wala code run honai degai, resources use kariagaa, user time consume hoga,
# server pai load jaigaa, yeh sab honai sai bachai-gai, using raise keyword, hum error raise kar daigai taaki agai ka code run na ho.



c = input("Enter your name: ")
try:
    print(a)
except Exception as e:
    if c == "harry":
        raise ValueError("Harry user is blocked")

    print("Exception Handled")