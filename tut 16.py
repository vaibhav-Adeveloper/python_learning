# for loop in python

# list1 = ["vaibhav","priyanshu","ishant","ayush"] # List
# print(list1[0],list1[1],list1[2])

# below is the application of for loop
# for item in list1:                # jitni badi list hai utni baar for loop chalega
#     print(item)   #4 tab(spaces)--indentation level--means we enter the foor loop
# details below of above loop
# pehlai item ki vlaue vaibhav hogi,phir priyanshu,phir ishant and so on ,for loop puri list kai end tak chalega
# har data type ko iterate nhi kar saktai hai

# for item in list1:  yeh likhnai ka matlab hai - jitni badi list hogi utni baar hi yeh for loop chalega
#     print(item)

# tup = ("vaib","pri","ish","ayu") # Tupple
# for item in tup:
#     print(item)

# List = [ ["Harry",1], ["Larry",2], ["Carry",6],
#         ["Marie",250] ]  # List in List /List of List.
# for item in List:
#     print(item)   # here item will be list--["Harry",1],["Larry",2]

# for item,lollypop in List:
#     print(item, "and lolly is", lollypop)  # item mai name aa jaiga (ex harry etc) and lollypop mai numbers aa jaigai
# print()

# TypeCasting
# converting list into dictionary
# we will use function -- dict()
# dict1 = dict(List)
# print(dict1)

# for item in dict1:    # keys will get printed
#     print(item)

# for item,lollypop in dict1:  # ERROR ERROR --will not work
#     print(item, "and lolly is", lollypop)

# TO do ITERATION in DICTIONARY have to use FUNCTION -- .items()
# in Dict,if want to print both KEY and its VALUE by ITERATION have to use function -- .items()
# for item, lollypop in dict1.items():
#     print(item, "and lolly is", lollypop)

# in Dict,if we want to print only KEY,no using of function,write it simply
# for item in dict1:   # if we want only KEY to print of Dict,we can do directly,no using of function -- items()
#      print(item)

# list ua kisi mai bhi present cheez ko ,jismai hum for loop chala rhai usmai present elements ko hi item kah rhai hai

# WE CAN ALSO USE IF,ELSE STATEMENTS IN FOR LOOP
# WAP to print item only if he eats less than 12 lollypop


# range kai andar koi bhi cheez number honi chaiye -- for i in range(len(string))
# for i in range(45):
#     print("hello")

# i ki value ZERO sai start hoti
# range() kai andar jo number likhtai hai wo Excluded hota hai
# for i in range(10):
#     print(i)    # output - 0 1 2 3 4 5 6 7 8 9

#  QUIZ
# make a list,print only numbers present in list which are greater then 6

lamp = [0,1,2,3,"harry",int,float,5.46,"hello","welcome",7,88,90,45,100,"merry"]
# for item in lamp:
#     if item.isnumeric() and item>6:  # ERROR
#         print(item)

for item in lamp:
    if str(item).isnumeric() and item > 6:    # .isnumeric() function is only defined for strings.
        print(item)

# Function
# --> isnumeric() - checks whether it is numeric or not
# remember - .isnumeric() function is only defined for strings.
