# More on files

# seek(), tell()

# tell() function kaaam aata hai yeh pta karnai kai ki file pointer kha par hai iss samai, tell func btata hai ki file kai kis character pai point ho rha hai
# seek() function file pointer ko RESET karnai kai kaam aata hai, matlb file kai kis character pai point karna hai uss samai, yeh hum bta saktai hai.

# f is a file handle or file pointer
f = open("vaibhav.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(11)  # File ko kha sai padna start karai
print(f.readline())  # 12 sai pura print kar diya(uses seek() function)
# print(f.tell())
f.close()