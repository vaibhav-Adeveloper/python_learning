# Time Module in python.
# use to calculate the execution time of a program.

# in time module we have time() function,,which gives no of ticks and 1 tick = 1 second.

import time

initial = time.time()   # Will gives some value
# print(initial)
# k = 1
# while(k<46):
#     print("Python Programmer")
#     k+= 1
# # print("while loop takes", time.time() - initial, "seconds")


# initial2 = time.time()
# for i in range(45):   # loop will run for 45 times.
#     print("Python Programmer")
# # print("for loop takes", time.time() - initial2, "seconds")


# one more time function.

localtime = time.asctime(time.localtime(time.time()))
# localtime = time.localtime(time.time())
# print(localtime)

# time.time() return no of ticks
# time.localtime() convert the ticks into local time but it returns the tupple
# time.asctime() converts the tupple given by time.localtime() into normal date form


# sleep() function kisi bhi cheez ko kuch seconds rook daita hai.

k = 1
while(k<46):
    print("Python Programmer")
    time.sleep(2)  # 2 ,2 seconds ka delay hota rhega ab in while loop
    k+= 1

print("while loop takes", time.time() - initial, "seconds")