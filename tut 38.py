# Using python - External and Built in MODULES

# press control key and click on the module, uss module ka code khul jaiga
# kisi bhi module ka code backened mai already likha hua hota hai

# REFER TO THE DOCUMENTATION FOR LEARNING MODULES IN PYTHON AND SUB MODULES AND FUNCTIONS PROVIDED INSIDE THAT MODULES.

# We can use sub modules and functions provided by those modules,which are in modules.

# NOTE : we can have sub-modules inside a module and then function in it of the module or we can directly have the functions of the module in it.

# generating the random number with the help of random module
# there are many functions inside random module
# some of the function of the random module
import random
# 1).
random_number = random.randint(0,5)  # 0 and 5 kai beech koi sa bhi integer mil sakta hai including 0 and 5
# print(random_number)

# 2).
rand = random.random()  # Will generate any random number between 0 and 1
# print(rand)
# If we have to generate any number between 0 and 80,so to do this just multiply it with that number
rand = random.random() *80
# print(rand)

# 3).
lst = ["Nasa","Isro","Cena","Jsa","Eena","Csa"]
choice = random.choice(lst)  # Will randomly choose any elements from the list
print(choice)

# EXPLORE MORE FUNCTIONS IN THIS MODULE BY GOING TO GOOGLE.COM