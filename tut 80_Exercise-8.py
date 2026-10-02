# Exercise-8
# oh soldier prettify my folder.

# function to take folder path as an input in string.
# input dictionary file - files which you dont want to manupulate/change in them.
# input - file format - png,jpeg,jpg etc.

# what to do - capitilise all the files name except those name which are in given dictionary file
# ex - dict. file contains : that, this, normal etc.
# we also don't have to manupulate with the given file format.
# but to these given file format - have to rename as 1.ff, 2.ff
# ex - gsd.jpg, ssf.jpg -- 1.jpg, 2.jpg etc.
# remember - only have to manupulate with the files directly inside the given file path, not have to touch the folders of the given file-path.


import os
# D:\PYTHON\tut 80_experiments
# path = "D:\PYTHON"
path = input("Enter the path: ")

dictFile_of_tut80 = input("Enter the dictionary file name: ")
inputs_in_file = int(input(f"Enter no of files name you want to enter in {dictFile_of_tut80}: "))
print("Start entering file names: ")
with open(dictFile_of_tut80, "w") as f2:
    for i in  range(inputs_in_file):
        file_name = input()
        f2.write(f"{file_name}\n")

forMat = input("Enter the file format: ")
# giving jpeg format to convert below images to 1.jpeg, 2.jpeg, 3.jpeg
# WhatsApp Image 2025-05-28 at 12.26.36 AM.jpeg
# WhatsApp Image 2025-05-28 at 12.26.36 AM (1).jpeg
# WhatsApp Image 2025-05-28 at 12.26.37 AM.jpeg


# print(os.listdir(path))
# print(os.scandir(path))
# print(path)

# for entry in os.scandir(path):
#     if entry.is_file():
        # print(entry)
        # print(entry.path)
        # a = str(entry)
        # print(type(entry))


def prettify_folder(path, dictFile, format):
    with open(dictFile, "r") as f:
        # creating a list that contains all the file name as its element, given in dictFile_of_tut80.
        leave_file = [element.strip() for element in f.readlines()]     # list comprehension.


    # capitilising the name of the files inside the given file path, leaving those file whose name are in dict_file.
    for entry in os.scandir(path):
        if entry.is_file():
            z = os.path.basename(entry.path)
            if z.split('.')[0] not in leave_file:    # checks that, that file name is there in dict_file.
                # a = os.path.basename(entry.path)
                b = z.capitalize()
                # os.rename(str(entry), str(entry).capitalize())
    # OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: "<DirEntry 'agentic_ai.py'>" -> "<direntry 'agentic_ai.py'>"
                os.rename(f"D:/PYTHON/tut 80_experiments/{z}", f"D:/PYTHON/tut 80_experiments/{b}")


    # renaming all the file, whose format is given by the user.
    # creating a list that contains all the file name as its elements with the given file format.
    # to create that list, either write:
    format_list=[]
    for entry in os.scandir(path):
        if entry.is_file():
            c = os.path.basename(entry.path)    #.split('/')[-1]
            d = c.split('.')[1]
            if d == format:  # checks that png, jpg, jpeg is written at last or not in that file.
                format_list.append(c)
    # OR
    # format_list = [(str(entry.is_file()).split('.'))[1] == format for entry in os.scandir(path)]    # list comprehension.
    # IndexError: list index out of range


    i = 1
    for element in format_list:
        os.rename(f"D:/PYTHON/tut 80_experiments/{element}", f"D:/PYTHON/tut 80_experiments/{i}.{format}")
        i = i + 1

    # for entry in os.scandir(path):
    #     if entry.is_file():
    #         # print(str(entry))
    #         print(entry)


prettify_folder(path, dictFile_of_tut80, forMat)

# print(os.path.basename(path))
# print(os.path.basename(path))


print("Code status: 200")   # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@