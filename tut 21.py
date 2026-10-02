# OPERATORS in python

# 1).Arithmetic OP
# help in numerical calculation
# they are --> + , - , * , /
# print("5 + 6 is", 5+6)
# print("5 - 6 is", 5-6)
# print("5 * 6 is", 5*6)
# print("5 / 6 is", 5/6)

# print("5 // 6 is", 5//6) # // Give the integer value,forget the values after decimal

# # // is floor division operator - ex- 14/3 gives output 14.333334 but 14//3 will ignore .333334 and gives output 14
# print("15 // 6 is", 15//6) # // Give the integer value,forget the values after decimal

# # ** is exponential OP --> it raises to the power
# print("2 raise to power 3 is",2**3)
# print("5 raise to power 3 is",5**3)

# # modulus OP - % - it gives remainder
# print("remainder of 17/5 is",17%5)


# 2).Assignment OP
# agar kisi variable mai value assign karna ho
# # ex -->  = , += , -= , /= , %=
# x = 5
# print(x)
# x += 7 # += operator iskai aagai jo likha hoga utni value iss variable x  mai jod daiga
# # x += 7  -- x = x + 7
# print(x)
# x -= 9   # x = x - 9
# print(x)
# x /= 2   # x = x / 2
# print(x)
# x = 5
# x %= 3   # x = x % 3
# print(x)

# 3).Comparison OP
# ex -->  == , != (not equal to), >,<, >= , <=
# i = 5
# print(i == 8)
# print(i != 4)
# print(i > 5)
# print(i >= 5)
# print(i <= 9)

# 3).Logical OP
# Uses when building the GUI
# ex --> AND .OR, NOT
a = True
b = False
# print(a and a)
# print(a and b)
# print(a or b)
# print(not a)
# print(not b)

# 4).Identity OP
# ex --> is , is not
# print(a is b)
# print(a is not b)
# print(5 is not 7)
# print(5 is not 5)

# 5).Membership OP
# ex --> in , not in
# list = [2,3,4.5,55,43.4,54,5,65]
# print(54 in list)
# print(544 in list)
# print(4 not in list)

# 6).Bitwise OP
# ex --> & (bitwise and) , | (bitwise or)
# ex --> these OP works with binary number 0,1
# 0 -- 00
# 1 -- 01
# 2 -- 10
# 3 -- 11

 # | is bitwise OR
 # & is bitwise AND

print(0 & 1) # 00 and 01 -- 0 and 0 is 0, 0 and 1 is 0, 00 & 01 is 00 and 00 is 0
print(0 | 1) # 00 or 01 -- 0 or 0 is 0, 0 or 1 is 1, 00 | 01 is 01 and 01 is 1
print(0 | 3) # 00 or 11 -- 0 or 1 is 1, 0 or 1 is 1, 00 | 11 is 11 and 11 is 3
print(5 & 4) # 110 and 100 -- 1 and 1 is 1, 1 and 0 is 0, 0 and 0 is 0, 101 & 100 is 100 and 100 is 4
print(0 & 2) # 00 and 10 -- 0 and 1 is 0, 0 and 0 is 0, 00 & 10 is 00 and 00 is 0