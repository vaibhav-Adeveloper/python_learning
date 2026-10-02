import os

# if we have to find, how many folders are there in the particular directory.
# we have a method that will gives all the folders availaible in the directory in the form of "List".

# folders = os.listdir("data")
# print(folders)

# AS folders is a list, now we can perform all availaible tasks of the list.
# print(len(folders))

# for folder in folders:
#     print(folder)

# we can access files inside the folder.
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

# explore os.system

# get current working directory.
# change current working directory.

print(os.getcwd())

# os.chdir("/Users")
# print(os.getcwd())