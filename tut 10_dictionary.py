# DICTIONARY -- is a DATA structure #
# key value pair ko MAP karta hai
# Dictionary is nothing but key value pairs
#
d1 = ()
print(type(d1))
d1 = []
print(type(d1))
d1 = {}
print(type(d1))

# making a dictionary,which tells us what they are in tech field
# ALSO WE CAN MAKE DICTIONARY INSIDE A DICTIONARY
d2 = {"Vaibhav":"Web Developer","Ishant":"App Developer",
      "Priyanshu":"Data Analyst","Lucky":{"PW":"App Developer","McKinsey":"Web Developer","OYO":"Video Editor"}}
# print(d2)
# print(d2["Vaibhav"])  # case sensitive
# print(d2["Priyanshu"])  # Priyanshu key kai coressponding jo bhi value hogi wo print ho jaigi
# print(d2["Ishant"])   # Ishant key kai coressponding jo bhi value hogi wo print ho jaigi
# print(d2["Lucky"])
# print(d2["Lucky"]["OYO"])
# KEY --Ishant, VALUE -- App Developer
# Lucky -- KEY, Dictionary --VALUE
# KEY can be number or string.

# Adding the Items in dictionary
# d2["Ayush"] = "Software Developer"  # this key-value pair will get added in dictionary d2.
# d2["Vinayak"] = "AI Engineer"       # this key-value pair will get added in dictionary d2.
# d2[10101011] = "Binary Language"
# print(d2)

# Deleting the key-value in dictionary,we will use -- del function
# del d2["Ayush"]
# print(d2)

# concept
d3 = d2  # here d3 is equal to d2, it doesn't means that a copy of d2 is made into d3
# any change to d3 will get reflected into d2.

# del d3["Vaibhav"]   # vaibhav key is also deleted from d2 dictionary
# print(d2)

# Functions in Dictionary
# 1. copy() --> make the copy of a dictionary.

d3 = d2.copy()  # now any change to d3 will not affect the d2, d2 will remains unchnaged on changing the d3.
del d3["Vaibhav"]
print(d2)

"""A important thing to focus"""
# 2. get()
print(d2.get("Ishant"))

# 3. update()
d2.update({"Ayush":"Toffee"})
print(d2)

# 4. keys()
print(d2.keys())  # will print all the keys in the form of list

# 5. items()
print(d2.items())   # will print all the key-value pairs as a list of tupple --> (key,value)

"""REFER TO GOOGLE,SEARCH
   PYTHON DICTIONARY FUNCTIONS"""