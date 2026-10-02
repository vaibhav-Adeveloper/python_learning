# code run perfectly
# f = open("tut 55_OOPS_3.py", "rt")
# a = f.read()
# f2 = open("tut 56_OOPS_4.py", "w")
# f2.write(a)
# f.close()
# f2.close()

# code run perfectly
# f = open("tut 55_OOPS_3.py", "rt")
# f2 = open("tut 56_OOPS_4.py", "w")
# f2.write(f.read())
# f.close()
# f2.close()

# code run perfectly
with open("tut 55_OOPS_3.py", "rt") as f:
    with open("tut 56_OOPS_4.py", "w") as f2 :
        f2.write(f.read())