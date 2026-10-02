# Try Except Exception Handling

# agar hum esi cheez run kar rhai hai apnai python code kai andar jismai error aa bhi sakta hai or error nhi bhi aa sakta hai

# print("Enter the number 1")
# num1 = input()
# print("Enter the number 2")
# num2 = input()
# print("The sum of these two numbers is", int(num1) + int(num2))
# # line 9 kai baad code run hi nhi hoga because error aa jaiga isliayi code iss error kai baad run hi nhi kraigaa
# line no 12 execute nhi ho paigi
# print("This line is very important to execute")

# agar isi cheez sai bachna ho, ki code mai error bhi aa jai toh usai bta dai and then uskai aagai kai code ko bhi run krai esa na ho ki error aatai hi code run karna ruk jai,
# code run karna rukai na error aanai kai baad bhi uskai aagai ka code bhi run ho and uss error ko program bta dai

# Now to do this we use concept of try except Exception handling
print("Enter the number 1")
num1 = input()
print("Enter the number 2")
num2 = input()
try:
    print("The sum of these two numbers is",
          int(num1) + int(num2))
except Exception as e:
    print(e)   # error will print as string


print("This line is very important to execute")

# as is a keyword
# We use this when we deal with internet connectivity