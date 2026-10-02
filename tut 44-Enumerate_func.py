# Enumerate Function.

# print only those programming language which is at odd place.

# lst = ["python","java","c++","javascript","CSS"]
# i = 1
# for item in lst:
#     if i%2 != 0:
#         print("vaibhav learn", item, "programming language")
#     i+= 1

# Doing the same with the help of F STRING
lst = ["python","java","c++","javascript","CSS"]
# i = 1
# for item in lst:
#     if i%2 != 0:
#         print(f"vaibhav learn {item} programming language")
#     i+= 1


# humai i = 1 "declare" karna pada, phir i += 1 "update" karna pada, matlb bahut kuch karna pada in the for loop to do our task.
# Inn cheezo ko hi short bana nai kai liyai, we use enumerate function.

# Syntax - Enumerate function takes both index and item.

for index, item in enumerate(lst):   # index start from 0
    if index%2 == 0:
        print(f"vaibhav learn {item} programming language")

# Humai doo kaam kam karnai pade phir bhi we get same output, we don't have to do i = 1 and i += 1, when using the Enumerate function.


# Note: Self:
# use Enumerate function with the for loop to make the 'for loop shorter', to reduce the number of lines in for loop.