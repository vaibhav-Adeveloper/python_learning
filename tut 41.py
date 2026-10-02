# *args and **kwargs in python.

# function printing the name of students
# def name_print(a,b,c,d):
#     print(a,b,c,d)
#
# name_print("vaibhav","priyanshu","ishant","zaid")

# To add more names we have to increase the arguments in function, have to add e,f etc
# def name_print(a,b,c,d,e):
#     print(a,b,c,d,e)
#
# name_print("vaibhav","priyanshu","ishant","zaid","rudra")

# now imagine if we have millions of user,so we will add all those users names like this
# doesn't we have another GOOD way to do this
# Here comes the concept of args.

# def funargs(*args):
#     print(type(args))     # <class 'tuple'>
#     print(args)
#     print(args[0])

# # hum args mai for loop bhi chala saktai hai
#
# lst = ["vaibhav","priyanshu","ishant","zaid","rudra"]
# funargs(*lst)     # sarai elements of the list store ho jaigai in the args.

# ALL ELEMENTS GOES IN THE FORM OF TUPPLE IN THE ARGS,WHETHER THEY ARE LIST,TUPPLE,etc


# def funargs(*args):
#     for item in args:
#         print(item)
#
# lst = ["vaibhav","priyanshu","ishant","zaid","rudra"]
# funargs(*lst)

# We can pass other arguments also other than args
# def funargs(normal, *args):
#     print(normal)
#     for item in args:
#         print(item)
#
# lst = ["vaibhav","priyanshu","ishant","zaid","rudra"]
# abc = 66
# funargs(abc,*lst)

# We can also write other names of args
# def funargs(*argsPython):
#     for item in argsPython:
#         print(item)
#
# lst = ["vaibhav","priyanshu","ishant","zaid","rudra"]
# funargs(*lst)

# add as many names as we want no worry of adding it
# def funargs(*args):
#     for item in args:
#         print(item)
#
# lst = ["vaibhav","priyanshu","ishant","zaid","rudra","ayush","anmol"]
# funargs(*lst)

# CONVENTION - we have to put first normal arguments,then args,then kwargs
#   normal arguments, args, kwargs   $$$$$$$$
# otherwise ERROR will come

# ERROR
# def funargs(*args,normal):
#     print(normal)
#     for item in args:
#         print(item)
#
# lst = ["vaibhav","priyanshu","ishant","zaid","rudra"]
# normal = " this is your programmer"
# funargs(*lst,normal)

# NO ERROR
# def funargs(normal, *args, **kwargs):
#     print(normal)
#     for item in args:
#         print(item)
#
# lst = ["vaibhav","priyanshu","ishant","zaid","rudra"]
# normal = "this is a python programmer"
# funargs(normal)


# Introducing Kwargs
# def funargs(normal, *args, **kwargs):
#     print(normal)
#
#     for item in args:
#         print(item)
#
#     for key, value in kwargs.items():
#         print(key, value)
#
# lst = ["vaibhav","priyanshu","ishant","zaid","rudra"]
# normal = "this is a python programmer"
# kw = {"vaibhav":"web developer","priyanshu":"researcher","ishant":"app developer"}
# funargs(normal,*lst, **kw)


def funargs(normal, *args, **kwargs):
    print(normal)

    for item in args:
        print(item)
    print("\nintroducing the kwargs and all about them,thier knowledge")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")    # used F-string.

lst = ["vaibhav","priyanshu","ishant","zaid","rudra"]
normal = "this is a python programmer"
kw = {"vaibhav":"web developer","priyanshu":"researcher","ishant":"app developer"}
funargs(normal,*lst, **kw)


# REFER TO DOCUMENTATION FOR DEPTH KNOWLEDGE OF THE CONCEPTS AND TOPICS