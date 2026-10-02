# using else with for loop.

# for loop kai sath else jab hi chalta hai jab for loop normally end ho, yaani for loop ko koi break statement na mile
# for loop doo tarikai sai end ho sakta hai
# agar jispai for loop chal rha hai, uskai sarrai element khatam ho jaai (normal end)
# agar for loop mai koi break statement reach ho jaai.

# " for loop kai else kai andar python ka control jab hi jaiga jab for loop normally end hoga, matlb break ki wajah sai end na ho
#  maltb aisa nhi hai ki break use nhi kar saktai hai, break use kar saktai hai, bas agar for loop break ki wajah sai end na ho, toh else
#  statement will execute. "

khana = ["roti", "dal", "chaawal", "sabzi"]
# for item in khana:
#     print(item)
#
# else:
#     print("This for loop ended properly")


# for item in khana:
#     print(item)
#     break
#
# else:
#     print("This for loop ended properly")


for item in khana:
    if item == "paratha":
        break
else:
    print("Your item was not found")