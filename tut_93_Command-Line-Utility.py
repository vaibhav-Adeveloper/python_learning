# Creating a Command Line Utility.

import argparse     # module used to create CLI's.
import sys

def calc(args):
    if args.o == "add":
        return args.x + args.y

    elif args.o == "mul":
        return args.x * args.y

    elif args.o == "sub":
        return args.x - args.y

    elif args.o == "div":
        return args.x / args.y

    else:
        return "Something went wrong."

if __name__ == '__main__':
    # ArgumentParser() is a class.
    # we will create the object of this class.
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="Enter first number, This is utility for calculation.")

    # adding argument in the console or in our command-line-utility by using the add_argument().

    parser.add_argument('--y', type=float, default=2.0, help="Enter second number, This is utility for calculation.")

    parser.add_argument('--o', type=str, default="add", help="This is utility for calculation.")
    # --o --> operation

    # now parsing all the given arguments.
    args = parser.parse_args()
    # see the backened implementation of the parse_args() function of ArgumentParser() class.

    # writing in our console.
    sys.stdout.write(str(calc(args)))

    # sys.stdout.write("statement to be printed in console")    # print the things in console.

# now to run your CLU:
# write in the powershell:  # basically reaching to this file in powershell.
# cd _  (this may required for you or may not)
# cd .\PycharmProjects\
# cd D:\PYTHON\
# python .\tut_93_Command-Line-Utility.py --x 4 --y 8 --o mul


# Task - make a faulty calculator CLU.
