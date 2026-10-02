import os

# print(dir(os))  # will display all the methods that are defined for os module and be used with it.


print(os.getcwd())


# os.chdir("D:\PYTHON\OS module\data\Concept_51")
# os.chdir("C://")
# print(os.getcwd())


# print(os.listdir())  # will give all files and folders of the cwd.
# print(type(os.listdir()))
# os.chdir("C://")
# print(os.listdir())
# print(os.listdir("C://"))


# os.mkdir("Python")  # will make the directory.
# os.makedirs("This/that")  # will make directory and its sub directory. to  make multiple directory.


# os.rename("D:\PYTHON\\tryOut.py", "D:\PYTHON\TryOut.py")
# os.rename("D:\PYTHON\TryOut.py", "D:\PYTHON\\tryOut.py")

# environment variables read
print(os.environ.get('Path'))
# print(os.environ.get('OS'))
# print(os.environ.get('TEMP'))
# print(os.environ)

# join function
# use to add two paths
# print(os.path.join("C://", "Vaibhav.txt"))

# exists() function
# print(os.path.exists("C://"))   # yeh directory exit karti hai.
# print(os.path.exists("C://Vaibhav"))    # esi koi bhi directory exit nhi karti hai.
# print(os.path.exists("C://Program Files"))

# isfile() & isdir() function
print(os.path.isfile("C://Program Files"))     # Program Files ek directory/folder hai, yeh ek file nhi hai.
print(os.path.isdir("C://Program Files"))