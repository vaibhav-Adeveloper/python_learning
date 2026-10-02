# for i in range(3):
#     print(i)
# else:
#     print("loop is executed")

num = 0
def addContact():
    name = input("Enter the name: ")
    mobile = int(input("Enter the number: "))
    # global dict
    # contact = dict.copy()
    # contact = dict.update({name: mobile})
    dict.update({name: mobile})
    print(dict)

if num < 1:
    num+=1
    dict = {}
    print("Your Contact dictionary is empty")
    choice = input("Do you want to add a contact :")
    if(choice.lower()=="yes"):
        addContact()
else:
    addContact()

