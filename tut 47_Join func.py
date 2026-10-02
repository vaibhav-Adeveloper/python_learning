# Join function in python.

list = ["john","cena","randy","khali","orton","sheamus"]
# lets say we have to print like john and cena and randy and ortan and khali and sheamus

for item in list:
    print(item, "and", end=" ")


# to do line 6 and 7 work we will use JOIN function

a = " and ".join(list)
print(a)

a = ", ".join(list)
print(a)


m = "vaibhav"
b = " sharma ".join(m)
print(b)