# Coroutines in python.
import time


# this means that ek particular lines of code tak function sirf ek baar run hoga, isskai baad run karogai toh ab suru sai run nhi hoga function
# usskai aagai sai run hoga (jitna pehli baar mai run ho gya tha)  aur jitni baar bhi run karogai function ko usskai agai sai hi run hoga.


# hum chahtai hai ki pehli baar function jab run ho toh shuru sai run hoga, lekin abb jab hum funntion dobara run kariagai, toh function
# shuru sai run na ho, ek particular jagah sai run ho
# ex --> 120 line of code hai, pehli baar run - pura 120 lines of code run hoga, lekin jab agli baar run karogai toh 50th line of code sai
# run hoga yeh code - this power is given by coroutines.

# let say we have a function searcher that reads a particular chapter from the book.
# and takes lots of time to read a chapter.
def searcher():
    import time
    # reading a chapter.
    # some 4s time consuming task.
    book = "a string containing 1000s of lines of chapter of the book. these books are good to read"
    time.sleep(4)   # code task
    # book ko read karnai kai baad hum chahtai hai ki hum kuch bhi dai toh yeh function find out karai ki yeh cheez uss book mai hai ki nhi.

    """ # concept - jab hum iss function ko ek baar run karai toh yeh yha tak run ho.
    # jab algi baar run karai toh yeh ab iskai agai sai run ho. 
    so to do this we use coroutines """

    while True:
        text = (yield)
        # jo bhi cheez mai searcher function ko send karungaa, wo iss text mai aa jaigaa.
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")



# this searcher is not a normal function but it is a coroutine.
# iss searcher ko start karnai kai liyai, humai use karna padega next() method ka.

search = searcher()   # we created the instance of the searcher function (coroutine).
next(search)
search.send("books")    # sirf iss case mai 4 second ka delay aaigaa - code line 18 - 34 will run
input("Press any key")
search.send("good")     # with fraction of seconds mai yeh execute ho jaiga. --> 0.0010840892791748047s - code line 28 - 34 will run
search.send("chapter")      # with fraction of seconds mai yeh execute ho jaiga. - code line 28 - 34 will run
input("Press any key")
search.send("Macbeth")      # with fraction of seconds mai yeh execute ho jaiga. - code line 28 - 34 will run

# searcher function sirf jab pehli baar run hoga toh hi sirf 4s laiga matlb book reading wla code execute kariagaa jo 4s lai rha hai,
# isskai baad app jitni baar bhi function ko run karogai, wo directly " while loop sai start hoga execute hona ".
# yaani sirf ek baar 4s rukna hoga, agli baar sai in fraction of seconds work hoga.

# next() method sai coroutine ka wo wala code run/execute hoga jo ki time lai rha hai, time consuming code block will run, on using next() method

search.close()


# Exercise:
