# comments,print statement and escape sequence

# Single line comments

"""
Multi
line
comments
"""

# comments are line which are neglected by python interpreter

# agar print karaigai toh automatically new line aaigi,see the example below
print("Welcome to python programming")
print("Lets learn python from basics to advanced")
print()
# Now to bring them(these statements) in single line,we have to use--> , end=""
print("Welcome to python programming", end=",")
print("Lets learn python from basics to advanced")
print()
print("Welcome to python programming", end=" ")
print("Lets learn python from basics to advanced")
print()
# Now to print two statements with the help of the single print function,how to do that
print("Welcome to python programming","Lets learn python from basics to advanced")
# comma gives the space when two statements are written in same print function.

"""to print thing as it with all enter,new paragraph, etc WE USE TRIPLE SINGLE QUOTE ''' ''' """
print('''STRUCTURE and CONTENT
         The handbook is divided into clear,concise chapters, each focused on a sprcific aspects of
         python:
         1.fundamental concepts: Start with the basics,such as installing python
          and writing your first program
         2.Practical examples:illustrative examples and sample code demonstrate the
         application of the concepts.
         3.Hand on exercise: 
           quality projects.
           active learning.''')

""" One thing to be remembered that-->
 comma(,) gives the space between two statements when used in print """
print()

# ABOUT ESCAPE SEQUENCE CHARACTER
# 1. about new line character--> \n (backslash n)--> gives new line
print("D:\nvaibhav")
print("hello vaibhav \n priyanshu  \nishant")
print()
print("C:\Harry")
print("C:\narry")
print("C:\\narry")

# 2. how to give a tab,use--> \t (backslash t)
print("vaibhav \tsharma")
print("vaibhav is a \ngood boy \t100")
# 3. To print single,double quote or backslash ',",\ in between statements,how to do this,have to use--> backslash quote --> \" \' or \\.
print("D:\\vaibhav")
print("D:\"vaibhav")
print("D:vaib\'hav\"shar\"ma")
