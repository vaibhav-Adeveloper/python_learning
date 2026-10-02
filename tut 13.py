# if_else_condition

# var1 = 6
# var2 = 56
# var3 = int(input())
# SYNTAX:
# if var3>var2:
#     print("Greater") # this automatic space given as we enter if condition is known as indentation
# if var3 == var2:
#     print("Equal")
# else:
#     print("Lesser")  # all three (if,if,else) will be checked.

# Now how python execute above if-else ladder.
# problem with above code is that if thus condition also hold true var3>var2 it will print Greater but still it will check further if condition that is written over their
# so to avoid this,means as soon as any condition hold true,program get execute out from if else ladder without checking further conditions,we have to use
# if , elseif (written as elif in python), else

# ERROR below
# if var3>var2:
# print("Greater") # no space is given -- error will occur.
# else:
#     print("Lesser")

# IN python elseif is written as elif.
# Good way to write is
# if var3>var2:
#     print("Greater")
# elif var3 == var2:
#     print("Equal")
# else:
#     print("Lesser")

# KEYWORDS
# 1.in
# 2. not in

# list1 = [5,7,3]

# print(5 in list1)  # returns true
# print(15 in list1)
# print(15 not in list1)

# if 5 in list1:
#     print("yes its in the list")

# not and in are two different keywords.

# QUIZ
# input a number(it will be age of human) and if it is of age above 18 print it can drive and vice versa and
# if its 18 age,it will be decided by physical verification that he/she can drive
print("Enter your age:", end=" ")
age = int(input())
if age < 10 or age > 100:
    print("Enter the proper age")
elif age > 18:
    print("Eligible for Driving")
elif age == 18:
    print("Either eligible for Driving or not for this confirmation you have to come for physical verification at RTO office")
else:
    print("Not Eligible for Driving")