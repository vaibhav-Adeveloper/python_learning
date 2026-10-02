import os
import shutil

# removing the folders/directory from directory.

# for i in range(0,50):
#     os.remove(f"data/Concept_{i+1}")

# above code will not work it will throw error.
# reason :- remove() method in os module is not capable of removing a directory/folders.
# it can only remove the files, which are inside directory/folders.

# os.remove() method in Python removes or deletes a file path. This method can not remove or delete a directory. If the specified path
# is a directory then OSError will be raised by the method.

# we can use rmdir() method of os module, to remove the directory.
for i in range(0,50):
    os.rmdir(f"data/Concept_{i+1}")

# OR

# rmtree() method of shutil module.

# rmtree() method of shutil module
# for i in range(0,50):
#     shutil.rmtree(f"data/Concept_{i+1}")
# above code will remove all directory/foders named Concept_1, Concept_2, Concept_3 and so on till Concept_50 , which are in the data directory/folder.