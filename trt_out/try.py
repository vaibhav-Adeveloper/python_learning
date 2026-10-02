name = input("Enter the name: ")
substr = name[0:2]
name = name.replace(substr, "", 1)
name = name + substr
print(name)