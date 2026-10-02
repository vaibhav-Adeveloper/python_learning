# Generators, iterators and iterable.

"""
iterable - aise python object jinkai liyai __iter__() , __getitem__() method define hota hai, agar hum uss py obj par yeh method run karaigai toh wo iterator pradaan karaigaa.
iterator - __next__() method define hota hai.
iteration - iterate karnai ki process ko iteration kehtai hai.
"""

# making a generator:
def gen(n):
    for i in range(n):
        yield i

"""
difference between
return - return statement ko dekh kai function laut jaigaa, iskai baad wo kuch nhi karaigaa.
print - print sttmt console mai prnt karta hai and function run hota rheta hai.
yield - on the fly, value generate karta hai, matlb yeh ek generator hai.
"""

g = gen(749534294)
print(g)    # otp :  <generator object gen at 0x000001EA6DF2C1E0>

# inhai hum kyu use kartai hai -  to save the ram.
# hum nhi chahtai ki itna bda number hum apni memory mai store karkai, apnai system ko slow kardai.

# humnai generator bna liya ek aisi cheez jo inn sabhi number ko generate karnai kai capable hai, lekin mai abhi karna nhi chahta generate, na mai
# store karna chchta hu apni ram mai, hum bas ussai khada karkai taiyrr kar laigai, ki jab bhi humai teri jarrurat hogi, hum tujhe iterate karkai
# prapt kar laigai.

#   Generator aise iterator hotai hai jinhai app sirf ek baar hi iterate kar saktai hai.

g1 = gen(4)
# print(g1.__next__())
# print(g1.__next__())
# print(g1.__next__())
# print(g1.__next__())
# print(g1.__next__())    # error StopIteration

for i in g1:
    print(i)


#  iterable
v = "vaibhav"
print(iter(v))
name = iter(v)
print(name.__next__())
print(name.__next__())
print(name.__next__())
print(name.__next__())
# print(v[1])

for c in v:
    print(c)


# Exercise :
# make fibonacci series and factorial with the help of generator.