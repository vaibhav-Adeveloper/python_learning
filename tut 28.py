# How to write in a file and Append in a file

# Append means to join the text in the end of a file

# WRITE MODE
# f = open("vaibhav2.txt", "w")   # vaibhav2.txt file will w in text mode
# f.write("python language is the best language") # this content will go in it
# f.close()

# APPEND MODE
# f = open("vaibhav2.txt", "a")
# f.write("python language is the best language\n")   # this content will get added as many times as we will run the program
# f.close()

# write mode - mai jo file mai hai content wo replace ho jaiga uss content sai jo humnai likha hai, jitni baar hum run karaigai, when we
# run file only in write mode.
# append mode - jo file mai content hai wo toh already as it is rhaega, bus jo content humnai likha hai wo aur add ho jaiga.

# to get how many character we have written - how to do that
# f = open("vaibhav2.txt", "w")
# a = f.write("python language is the best language")
# print(a)
# f.close()

# how to open the file in both mode read and write
# Handle read and write both
f = open("vaibhav2.txt", "r+")
# a = f.write("python language is the best language")
print(f.read())
f.write("Thank you")
f.close()