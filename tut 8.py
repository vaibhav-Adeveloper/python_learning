# STRING FUNCTIONS
mystr = "Vaibhav is a python programmer"  # STRING
mystr2 = "VaibhavIsAPythonProgrammer"     # STRING
mystr3 = "vaibhav is a python programmer"  # all small letter
print(mystr)

# STRING = combination of characters.
"""In Python--> Index Starts From Zero"""

# if we want the part of the string --> "SLICING"
# In how many ways we can do this,let see it
print(mystr[3])  # Third index pai jo character present hai in mystr variable,wo print ho jaiga.

#### STRING SLICING rule ####
""""# print(mystr[2:6])
# print(mystr[from here:to this]) 
print(mystr[index:index]) 
# print(mystr[it is included:it is excluded]) """
print(mystr[2:17])

### LENGTH FUNCTION --> len(variable name) ###
# to print the lenght of a string.
print(len(mystr))
print()
print(mystr[0:30])
"""
index is from 0 to 29.
length is from 1 to 30.
"""
# print(mystr[55])  # ERROR
print(mystr[0:70])  # it give till where it is possible
print()

print(mystr[0:])  # by default takes its length
print(mystr[:5])  # starts from zero by default
print(mystr[:])  # from 0 to length
print(mystr[::])  # by default takes gap of 1
print()

# ADVANCED SLICING #
""" print(mystr[index start(included):index end(excluded):GAP]) """
print(mystr[0:7:2])  # 2--> ek ek character skip hota chala jaiga
print(mystr[0:7:3])  # 3--> doo doo character skip hota chala jaiga
print(mystr[0:7:6])  # 8--> five five character skip hota chala jaiga

# NEGATIVE INDEXES #
# in mystr string - in last programmer is written, r is -1 index,e is -2 index,m is -3 index, g is -7 i.

print(mystr[-9:-4])
# above slicing is equals to
print(mystr[21:26])

print(mystr[::-1])  # negative gap will reverse the string
print(mystr[::-2])  # will reverse the string and print the characters with one-one gap.

# FUNCTIONS #
print()
print(mystr.isalnum())
# alpha numeric string means string with no spaces.
print(mystr2.isalnum())

print(mystr.isalpha())
# checks for alpha numeric string
print(mystr2.isalpha())

print(mystr.endswith("programmer"))
print(mystr.endswith("program"))

print(mystr.count("a"))

print(mystr3)
print(mystr3.capitalize())  # will make the first letter of the string capital -- (v -> V)

print(mystr.find("python"))  # Gives the starting index of python in statement.
print(mystr.lower())  # convert to lower case
print(mystr.upper())  # convert to upper case
print(mystr.replace("python","java"))

"""REFER TO GOOGLE,FOR
   ALL (STRING FUNCTIONS IN PYTHON)"""
"""w3schools.com"""