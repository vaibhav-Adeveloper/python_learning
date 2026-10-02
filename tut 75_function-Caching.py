# Functon Caching in Python.

from time import sleep
from functools import lru_cache

@lru_cache(maxsize=3)
def some_task(n):
    # some task taking n seconds to execute
    sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    # below three value will be cached.
    some_task(3)
    some_task(2)
    some_task(5)
    print("Done... Calling again")
    some_task(3)
    print("Called again")
    some_task(5)
    print("I called it by giving value 5 in the function")

# mai nhi chahta hu ki yeh 3s ka delay aai, ek baar func ko run karnai kai baad.
# we do func caching by using lru_cache from functools module.
# lru_cache is a decorator.
# maxsize means app kitni value ko cache karna chahatai hai, app jitni value ko cache karaigai, wo utni value khaigaa in memory.
# maxsize = 3 means, meri pichli 3 calls ko save karkai rakhna. latest three calls will be saved in the memory, to save time when they are called once again.

# pura function dubara chalanai ki jagah, wo direct cache mai sai function ki return value ko retrieve kar laiga.


# Exercise:
# take a input from the user, that how many value he wants to cache
