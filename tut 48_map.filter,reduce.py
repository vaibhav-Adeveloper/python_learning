# About -- Map, Filter, Reduce

# MAP function - kisi bhi ek function ko ek puri list mai apply kar deta hai

numbers = ["3","5","43","50","64","55"]

# numbers[2] = numbers[2] + 2  # ERROR - adding the string with the integer

# converting the elements of list from string to numbers
# for this we have to do typecasting

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# print(numbers)
# numbers[2] = numbers[2] + 5
# print(numbers[2])

# kab tak for loop chala-tai rhogai har cheez kai liyai
# line 12 and 13 ka kaam jo doo line mai kiya hai wo hum ek hi line mai kar saktai hai
# with the help of MAP function , one line mai kaam kar saktai hai
# SYNTAX -

# map(first argument is - wo argument daina hai - wo function jo aap chatai hai ki uskai saarai element mai apply ho jai, Dusra argument - kis pai apply karna chatai ho yeh function).

# map(function jo saarai elements mai apply karna chahtai ho, jispai apply karna chahtai ho)

# map(int, numbers)
# map function returns the object.

# print(map(int, numbers))   # 0x000001D810ADC3A0 is a memory location

# map is a object, map returns the objects
# so we have to typecast the map object into list/ convert the object return by the map function into list

# numbers = list(map(int, numbers))   # Working-numbers naam ki list mai enter hua and int function chala diya, matlb saarai elements ko int mai convert kar dega
# print(numbers)
# OR
# print(list(map(int, numbers)))

# numbers[2] = numbers[2] + 5
# print(numbers[2])


# more example of map function

# def sq(a):
#     return a*a

# num = [1,2,3,4,5,6,7,8,9,10]
# square = list(map(sq, num))
# print(square)


# doing above thing with the lambda function
# lambda function is ONE LINER FUNCTION

# num = [1,2,3,4,5,6,7,8,9,10]
# square = list(map(lambda x : x*x, num))
# print(square)
# lambda x : x*x = ek aisa function jisko x pak-rha-rhai, toh wo uska square (x*x) kar kai return kar dega


# map function application
# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))  # lambda x:x(i) ek aisa function jisko x do toh wo x(i) return karaiga ,yha pr x ek function hai
#     print(val)

# what we have do above
# by using for loop we have taken element from 0 to 4,


# FILTER function - filter karta hai matlb ek esi list banata hai elements ki jispai given function true return karta ho

# list_1 = [1,2,3,4,5,6,7,8,9]

# def is_greater_5(num):  # iss func ko number daigai and yeh function true return karaiga if numb is greater than 5 otherwise false
#     return num>5

# How to use filter
# SYNTAX -
# filter(function, iterable)

# gr_than_5 = filter(is_greater_5, list_1)   # we have to typecast to list, otherwise if we print this without typecasting it into list - filter object location will be printed
# gr_than_5 = list(filter(is_greater_5, list_1))  # we dont want to print filter object, we want to print the list that why we have to typecast it to list
# print(gr_than_5)
# output : [6,7,8,9]

# jin jin elements kai liyai wo function true return karaiga, unn element ko laikar filter function ek list create kar dega.


# REDUCE function - it is a part of the functools module

from functools import reduce

list = [1,2,3,4]

# adding the elements of the list
# num = 0
# for i in list:
#     num = num + i
# print(num)

# doing the above things (line 89 to 92) in one line

# SYNTAX -
# reduce(jo app karna chahtai ho - uska function, kis pai yeh apply karna hai)

num = reduce(lambda x,y : x+y, list)
print(num)

num = reduce(lambda x,y : x*y, list)
print(num)
