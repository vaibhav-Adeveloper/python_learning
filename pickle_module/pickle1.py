# Har cheez python mai ek object hoti hai.
import pickle

# iss list ko preserve karna hai. iss list ko as it is file mai pickle karkai daal daina hai.

# iss module ki madat sai hum iss object(list) ko pack karaigai iss file mai.
# Pickling a python object (packing).
# cars = ["Audi", "Ferrari", "Porsche", "Maruti Suzuki"]
# file = "mycar.pkl"
# fileObj = open(file, "wb")
# pickle.dump(cars, fileObj)
# fileObj.close()
# dump() method of pickkle module takes two arguments, first is 'object to be packed' and second is 'file object'.


# how to Depickle the object (depacking).
file = "mycar.pkl"
fileObj = open(file, "rb")
mycar = pickle.load(fileObj)
# load() function takes file object as an argument, and returns a python object.
print(mycar)
print(type(mycar))


# Task1 -
# pickle.loads() ?