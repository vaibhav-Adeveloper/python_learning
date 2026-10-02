# Difference between 'is' and '=='

"""
== --> value equality - 'Two objects' have the same value.
is --> reference equality - Two references refer to the 'same object'.
"""

a = [4, 5, 6]
b = a
# b and a dono ek hi object ko point kar rhai hai, aisa nhi hai ki a ki copy ban kai b mai and store ho gyi ho b mai.
print(b == a)
print(b is a)

# b and a dono ek hi object ko point kar rhai hai, islyai agar b ko change karogai toh a bhi bhi change ho jaiga.
b[0] = 10
print(a)

# making copy of a
c = a[:]    # slicing.
print(c == a)
print(c is a)


x = [4, 9, "34"]
y = [4, 9, "34"]
print(y is x)
