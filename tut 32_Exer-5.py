# Exercise-5
# Health Management System

# log or retrieve
# for whom
# Total 3 clients - harry,praful,sparsh.
# Total 6 files.
# Write a function that when executed takes as input client name.
# one more function to retrieve  exercise or food/diet for client

def getdate():
    import datetime
    return datetime.datetime.now()

print("Want to log current progress, press 1 OR Want to retrieve previous progress, press 0 :-")
n = int(input())
print("press \"e\" for Exercise or \"d\" for Diet :-")
choice = input()
print("Enter your name: ", end="")
name = input()
name = name.lower()

def diet():
    if n == 0 and name == "harry":
        ret_harryDiet()

    elif n == 1 and name == "harry":
        log_harryDiet()

    elif n == 0 and name == "praful":
        ret_prafulDiet()

    elif n == 1 and name == "praful":
        log_prafulDiet()

    elif n == 0 and name == "sparsh":
        ret_sparshDiet()

    elif n == 1 and name == "sparsh":
        log_sparshDiet()
    else:
        print("This user have not join our membership")
        return

def exercise():
    if n == 0 and name == "harry":
        ret_harryExer()

    elif n == 1 and name == "harry":
        log_harryExer()

    elif n == 0 and name == "praful":
        ret_prafulExer()

    elif n == 1 and name == "praful":
        log_prafulExer()

    elif n == 0 and name == "sparsh":
        ret_sparshExer()

    elif n == 1 and name == "sparsh":
        ret_sparshExer()

    else:
        print("This user have not join our membership.")
        return

def ret_harryDiet():
    f = open("Harry.txt", "r")
    print(f.read())

def log_harryDiet():
    # f = open("Harry.txt", "x")
    print("Write your progress: ")
    f = open("Harry.txt", "a")
    prog = input()
    time = getdate()
    f.write("\n" + str(time) + ", --> " + prog)

def ret_prafulDiet():
    f = open("Praful.txt", "r")
    print(f.read())

def log_prafulDiet():
    # f = open("Praful.txt", "w")
    # write logic if file doesn't exit, make it and if it already exit don't male it just add the content in it.
    f = open("Praful.txt", "a")
    print("Write your progress: ")
    prog = input()
    time = getdate()
    f.write("\n" + str(time) + ", --> " + prog)

def ret_sparshDiet():
    f = open("Sparsh.txt", "r")
    print(f.read())

def log_sparshDiet():
    # f = open("Sparsh.txt", "x")
    print("Write your progress: ")
    f = open("Sparsh.txt", "a")
    prog = input()
    time = getdate()
    f.write("\n" + str(time) + ", --> " + prog)

def ret_harryExer():
    f = open("Harry.txt", "r")
    print(f.read())

def log_harryExer():
    # f = open("Harry.txt", "x")
    print("Write your progress: ")
    f = open("Harry.txt", "a")
    prog = input()
    time = getdate()
    f.write("\n" + str(time) + ", --> " + prog)

def ret_prafulExer():
    f = open("Praful.txt", "r")
    print(f.read())

def log_prafulExer():
    # f = open("Praful.txt", "x")
    f = open("Praful.txt", "a")
    print("Write your progress: ")
    prog = input()
    time = getdate()
    f.write("\n" + str(time) + ", --> " + prog)

def ret_sparshExer():
    f = open("Sparsh.txt", "r")
    print(f.read())

def log_sparshExer():
    # f = open("Sparsh.txt", "x")
    print("Write your progress: ")
    f = open("Sparsh.txt", "a")
    prog = input()
    time = getdate()
    f.write("\n" + str(time) + ", --> " + prog)


if choice == "d":
    diet()
else:
    exercise()


# print("want to clear out your responses")
# print("Press y for yes and n for no: ", end="")
# cl = input()

# features to add:
#   sorry, no progress found - if it is first time retrieving the data

# def clear_out():
#     print("\nWant to clear your progress")
#
# clear_out()