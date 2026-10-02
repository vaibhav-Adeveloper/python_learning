# SET -- Data Structure
# relate with class 11 set chapter in math
#  it is a collection of well defined objects
s = set()  # empty set
# print(type(s))
# We can input elements in set from functions of set
# but the best way to do this is from LIST.

# l = [1,2,3,4,5]
# s_from_list = set(l)
# s_from_list = set([1,2,3,4,5])
# print(s_from_list)
# print(type(s_from_list))

# FUNCTIONS in set
# 1(a). How to add an element in empty set,we use add()
s.add(1)
# s.add(1)  # set retains only unique value(sirf unique value ko hi rhakega)
# set contains only unique value, it does not contain repeating values -- IMPORTANT
s.add(2)
# s.add(3,4,5)  # set.add() takes exactly one argument  # error will occur
# print(s)

# 1(b). union with other set
# s1 = s.union({8,9,0})
s1 = s.intersection({1,5,6})
print(s, s1)
print(len(s)) # print length of a set s
print(min(s)) # give minimum value present in set s
print(max(s)) # give maximum value present in set s

# 2. other functions
# difference,symmetric difference,disjoint
s2 = {4,6}
print(s.isdisjoint(s2))

s2.remove(4)
print(s2)

"""REFER TO GOOGLE
   SETS IN PYTHON"""