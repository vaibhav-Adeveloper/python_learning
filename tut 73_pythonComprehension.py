# Python Comprehension :-.

# list comprehension
# dictionary comprehension
# set comprehension
# generator comprehension



# let say we want a list comprises of elements divisible by 3.
# lst = []
# for i in range(100):
#     if i%3==0:
#         lst.append(i)

# print(lst)

# we can do above work in lesser line of codes.
# we can make above list in one line of code, with the help of list comprehension.
# list comprehension syntax:

lst = [i for i in range(100) if i%3==0]
# print(lst)


# dictionary comprehension
# dict = {i+1:f"item{i+1}" for i in range(9, 100) if (i+1)%20==0}
dict = {i:f"item{i}" for i in range(5)}
print(dict)

# to reverse the key-value pair of the dictionary, we can use dictionary comprehension.
dict = {value:key for key, value in dict.items()}
print(dict)


# set comprehension
# difference is that - value sirf ek baar hi li jaati hai.

dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
print(dresses)
print(type(dresses))


# generator comprehension
# generator ek aise function hotai hai jo yield karta hai, matlb jiskai pass generate karnai ki capability hoti hai lekin generate nhi kartai
# jab hum chahyai tab hum generator ko iterate kar kai ussai cheezo ko generate kar saktai hai, on the fly cheezo ko generate kar saktai hai.

def evenGen(n):
    for i in range(n):
        if (i+1)%2==0:
            yield i+1

num = evenGen(12)
print(num)
for i in num:
    print(i)

# doing above task with the help of # generator comprehension.

# to make generator comprehension we have to use parenthesis ()
even = (i+1 for i in range(100) if (i+1)%2==0)
print(type(even))
# generator ek special type kai iterator hotai hai, jinhai app sirf ek baar hi iterate kar saktai hai.
for num in even:
    print(num)


# Exercise:
# take a list - input from the user, ask to the user how many element they want in list, enter the element in it, then ask to the user
# which comprehension they want to make lst,dict,set and make it and then print it.