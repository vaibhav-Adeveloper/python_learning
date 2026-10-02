# python file IO

# lets learn how to write in a file
# we have created vaibhav.txt file

# SYNTAX -- TO READ A FILE
# we use open() function
# open("file name", "in which mode we want to open the file")

# Creating the file pointer
# open function return the value in the file pointer
# now we can do anything with file pointer
# we have to create a file pointer

# f = open("vaibhav.txt")
# content = f.read()  # we use read() function to get content of the file
# print(content)
# f.close()  # closing the file

# f = open("vaibhav.txt", "r")  # read mode
# content = f.read()
# print(content)
# f.close()

# r can be in text mode or binary mode

# f = open("vaibhav.txt", "rb")  # binary form,content will be read in binary form
# content = f.read()
# print(content)
# f.close()

# f = open("vaibhav.txt", "rt")  # text mode - read in the text form - default mode
# content = f.read()  # will read all the content of the file
# print(content)
# f.close()

# f = open("vaibhav.txt", "rt")
# content = f.read(4)  # only four character will be readed
# print(content)
# f.close()

# f = open("vaibhav.txt", "rt")
# content = f.read(4)  # only four character will be readed
# print(content)
#
# content = f.read(4)  # will read next four character
# print(content)
# f.close()


# if want to read character by character,the content of the file then we have to iterate the content of the file.
# f = open("vaibhav.txt", "rt")
# content = f.read()
# for line in content:
#     print(line)
# f.close()

# if want to read line by line,the content of the file then we have to iterate the content of the file.
# f = open("vaibhav.txt", "rt")
# # content = f.read()
# for line in f:
#     print(line, end="")
# f.close()

# jab bhi app file pointer ko read kartai hai (f.read()) - toh file pointer khali ho jata hai.
# iskai baad agar aap file pointer ko print karaigai toh kuch bhi nhi hoga kyunki file pointer khali hai

# About readline() function
# f = open("vaibhav.txt", "rt")
# print(f.readline())       # will read the first line
# print(f.readline())       # will read the second line
# print(f.readline())       # will read the third line
# f.close()

# About readlines() function
# it stores all the lines in a list
f = open("vaibhav.txt", "rt")
print(f.readlines())  # it will print the list which have lines in it
f.close()
