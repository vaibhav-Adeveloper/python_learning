# All about LIST.
# LIST --> DATA TYPE
# LIST DATA STRUCTURE/TYPE
thingsToBuy = ["laptop","phone","watch","clothes",
               "google", 1000, 145]
print(thingsToBuy)
print(thingsToBuy[2])   # index 2 pai present element aa jaiga jo thingsToBuy list mai hai.
print(thingsToBuy[5])   # index 5 pai present element aa jaiga jo thingsToBuy list mai hai.
numbers = [2,44,67,9,8,10,6,4]    # LIST
print(numbers)
print(numbers[3])

# LIST METHODS #
# 1.
numbers.reverse()  # method
print(numbers)
# it returns the list but will change the original list.

# 2.
print(numbers.sort())
numbers.sort()   # method
print(numbers)
# it returns the list but will change the original list.

# 3.
# print()
# numbers.sort()
# numbers.reverse()
# print(numbers)

# 4.
# len() function to calculate length of list,string.
print(len(numbers))

# 5. SLICING
numbers2 = [3,12,54,7,98,101,65]
# default value
print(len(numbers2))
print(numbers2[:7])  # by default it take 0 as starting
print(numbers2[0:])  # by default it take its length as ending
print(numbers2[:])  # by default it take its 0 as starting and length as ending
print(numbers2[2:])  # by default it take its length as ending
print(numbers2[1:5])
# slicing - it returns a new list but will not change the original list
print()

# 6.Extended Slicing
print(len(numbers2))
print(numbers2[::]) #--> by default it will take--print(numbers2[here 0:here its length:here 1])
print(numbers2[::2])  # it will skip one one element
print(numbers2[::3])  # it will skip two two element
print(numbers2[2:6])

# Negative slicing
print(numbers2[::-1])  # List will get reversed #
print(numbers2[::-2])  # List will get first reversed then it will skip one one element #
print(numbers2[::-3])  # List will get first reversed then it will skip two two element #
print(numbers2[1:5:-3])  #  It will not work.
print(numbers2[1:5:-1])  # IT WILL NOT WORK

# 7. max() function--gives max value of list that is present in it.
print(max(numbers2))
print(min(numbers2))

# 8. TO add a element in the END of the list,we use-- append(value) function.
numbers2.append(1000)
numbers2.append(100)
print(numbers2)

# 9. to insert the element in any index ,how to do this
# we have to use insert() function,how to give value in it
# insert(kis index mai value enter karni hai, that value)
numbers2.insert(2,18)
print(numbers2)

# 10. to remove a element in the list we use --remove(value) function
# numbers2.remove(1000)
# print(numbers2)

# 11.to remove the last element of the list,we use pop() function
numbers2.pop()
print(numbers2)
#
numbers2[1] = 72
print(numbers2)

"""
 MUTABLE--can change
 IMMUTABLE--cannot change
    
 list is mutable
 tupple is immutable
   () is parenthesis"""

# forming the tupple

# tp = (1,2,3,4)
# print(tp)
# tp[1] = 90  # CANNOT DO THIS
# print(tp)   # ERROR

"""Thing to NOTE"""
# if we want to make the single element tupple,so remember we have to apply a extra COMMA(,)
# tp = (1)  # tupple not form
# print(tp)
tp = (1,)
print(tp)
print()

# how to SWAP a two numbers.
# SWAP -- to interchange the value of the variable
# TRADITIONAL METHOD to do this
"""a = 1
b = 8
temp = a
a = b
b = temp
print(a,b)"""

# TO DO THIS WITH THE HELP OF PYTHON
a = 1
b = 8
a,b = b,a
print(a,b)

"""REFER TO GOOGLE,SEARCH
   PYTHON LIST FUNCTIONS"""