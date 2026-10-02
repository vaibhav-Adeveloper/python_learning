# Divide the apple !

n = int(input("Enter the number of apples harry must have: "))
mn = int(input("Enter the lower range of student: "))
mx = int(input("Enter the upper range of student: "))

if(mn==mx):
    print("This is not a range.")
    if(n%mn==0):
        print(f"{mn} is a divisor of {n}")
    else:
        print(f"{mn} is not a divisor of {n}")
else:
    for i in range((mx-mn)+1):
        if(n%(i+mn)==0):
            print(f"{i+mn} is a divisor of {n}")
        else:
            print(f"{i+mn} is not a divisor of {n}")