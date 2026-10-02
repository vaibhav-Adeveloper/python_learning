# How IMPORT works in python

# The 'sklearn' PyPI package is deprecated, use 'scikit-learn' rather than 'sklearn' for pip commands.

# Use 'pip install scikit-learn' rather than 'pip install sklearn'
#       - replace 'sklearn' by 'scikit-learn' in your pip requirements files

import sklearn as sk
print(sk.__version__)

# koi module kha sai laigaa, kaise laiga - yeh jannai kai liyai ek module hota hai.

import sys
print(sys.path)

# sys.path humarai wo saarai path hotai hai jha sai yeh sarai MODULE laikai aayega
# import sklearn likha toh yeh kha sai yeh module laiga
# so sys.path gives the hierarchy for this, first it will go to__ and find the module and then __ etc
# ['D:\\PYTHON', 'D:\\PYTHON', 'C:\\Python 3.12\\python312.zip', 'C:\\Python 3.12\\DLLs', 'C:\\Python 3.12\\Lib', 'C:\\Python 3.12', 'C:\\Python 3.12\\Lib\\site-packages', 'C:\\Python 3.12\\Lib\\site-packages\\win32', 'C:\\Python 3.12\\Lib\\site-packages\\win32\\lib', 'C:\\Python 3.12\\Lib\\site-packages\\Pythonwin']

# 'D:\\PYTHON' yeh wo hi directory hai jismai hum abhi hai


# from sklearn.ensemble import RandomForestClassifier
# print(RandomForestClassifier())

# we can import any python file in our current working file - how ?

# import file2
# print(file2.a)   # this method is good to import.

# from file2 import a
# print(a)

import file2
print(file2.a)  # file2.a means yeh file2 mai jaiga and then 'a' variable ko dhundai-ga
print(file2.funjokes("this is me"))

# There are already variables which have a global scope by defalut.
# int, float, __name__