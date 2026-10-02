# Using WITH BLOCK to open python files.

# rt mode is a default mode - open("vaibhav.txt", "rt")
# WITH BLOCK mai file ko close karnai ki jarrurat nhi hai

# with open("vaibhav.txt") as f:
#     a = f.read(4)
#     print(a)

with open("vaibhav.txt") as f:
    a = f.readlines()
    print(a)

f = open("vaibhav.txt")
print(f.readline())

# after the with block
# if we again open the file and use realines() function and close it
# will the file be printed (read) - yes or no and why ?

# No
# reason - file pointer khali ho jaiga pura
# kyunki readlines sai saari lines read ho jaigi, and last mai kuch nhi bachaiga file pointer kai pass read karnai kai liyai.