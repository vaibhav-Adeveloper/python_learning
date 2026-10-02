# WHILE LOOP
# SYNTAX --
# while(condition):  # jb tak yeh condition true rhegi jb tak loop chalta rhega
#     print(i)
#     condition update statement

# DIFFERENCE between for loop and while loop--
# for loop jab tak chalta tha jb tak humari list,dictionary,yha jispai bhi for loop chala hai jb tak uska content khatam na ho jai.
# while loop jb tak chalta jb tak given condition true rheti hai

i = 0
while(i<45):
    print(i)
    i = i + 1

# Agar ek line mai saarai numbers ko print karana hai,then we have to use
# end = " "
i = 0
while(i<45):
    print(i + 1, end=" ")
    i = i + 1