import os

# we have a method to check that if directory already exit, it will not make it but if directory does not exit, it will make it.
# to prevent this error - FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'data'
# 2.
if(not os.path.exists("data")):
    os.mkdir("data")

# 1. will make the new directory.
# os.mkdir("data")

# we have to make the 100 folders in the data directory but not one by one, directly make at once 100 no of folders.
for i in range(0,100):
    os.mkdir(f"data/Concept_{i+1}")


print(dir(os))  # this dir func will show all the availaible methods, attributes present in the os module.