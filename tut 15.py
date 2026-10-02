# EXERCISE-2--> Faulty calculator

# how to do this
# 1.first take input of 'operator' from user to be used
# 2.then take 'two number' on which operation to be done

# QUESTION --
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator and the two numbers as input from the user
# and then return the result

op = input("Enter the operator:")
n1 = int(input("Enter the number 1:"))
n2 = int(input("Enter the number 2:"))

if n1 == 45 and n2 == 3 and op == "*":        # if write op == * --> throw ERROR
      print("Result of calculation is:", 555)
elif n1 == 56 and n2 == 9 and op == "+":      # if write op == + --> throw ERROR
      print("Result of calculation is:", 77)
elif n1 == 56 and n2 == 6 and op == "/":      # if write op == / --> throw ERROR
      print("Result of calculation is:", 4)
# else:
#     print("Result of the calculation is:", n1 + int(op) + n2)   # ERROR ho rha hai essai toh
#     print(6 + 5)
elif op == "*":
    print("Result of the calculation is:", n1*n2)
elif op == "+":
    print("Result of the calculation is:", n1+n2)
elif op == "-":
    print("Result of the calculation is:", n1-n2)
else:
    print("Result of the calculation is:", n1/n2)
