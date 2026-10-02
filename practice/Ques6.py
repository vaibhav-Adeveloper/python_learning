# File IO, map, lambda.
# clear your concept, find the reason.

f = open("Ques6-file1.txt", "rt")

#########################
# below code will print numbers from 2 to 21 in file2 from file1, it will skip the number 1, it will not print the number 1 in file2.
# for item in f:
#     content = f.read()
# f2 = open("Ques6-file2.txt", "w")
# f2.write(content)
# f.close()
# f2.close()
######################

####################
# below code will not print any numbers in the file2
# for i in range(21):
#     content = f.read()
# f2 = open("Ques6-file2.txt", "w")
# f2.write(content)
# f.close()
# f2.close()
####################

###################
# below code will run perfectly
# will print all numbers from 1 to 21 in file2 from file1.
# a = f.read()
# for num in a:
#     content = a
# f2 = open("Ques6-file2.txt", "w")
# f2.write(content)
# f.close()
# f2.close()
##################

##################
# below code will print this in file2 : <map object at 0x000001A45C53C4C0>
# a = f.read()
# for num in a:
#     b = str(map(lambda x : x*2, a))
# f2 = open("Ques6-file2.txt", "w")
# f2.write(b)
# f.close()
# f2.close()
##################