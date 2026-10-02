# Decorators in python
# it used to modify the functionality of a function.

# func2 = function1()  -- agar parenthesis () laga daitai hai toh function1 call ho jata hai
# func2 = function1  -- agar parenthesis () na lagai toh function1 call nhi hoga lekin function1 ka work,matlb jo kuch bhi hai uskai andar wo sab func2 variable mai assign ho jata hai.
# func2 = function1 -- basically function1 ki copy ban gyi ek and wo copy of function1 function is func2, function1 ka jo kuch bhi tha wo sab func2 mai store ho gya hai.
# function1  func2 mai save ho jaiga

# def function1():
#     print("Learn Python")

# func2 = function1
# func2()

# func2 = function1
# del function1  # func() ki call karnai sai pehlai function1 ko delete kar diya, toh kya ab iskai baad func call hoga,func work karaiga
# func2()


# 1). hum function kai dwara ek function ko bhi return kar saktai hai
# def func_return(num):  # this function returns the function
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = func_return(0)
# print(a)

# 2). hum function ko as an argument bhi dai saktai hai
# def executor(func):
#     func("this is python")
#
# executor(print)


# Now here comes the concept of decorator.

def dec1(func1):  # this dec1 function takes the function func1 as an arguments and have another function inside it and before calling the func1 we do something and after calling the func1 we do something
    def now_exec():
        print("Executing Now")  # can do anything here before calling the func1
        func1()  # func1 ko execute kar diya jo dec1 function nai liya
        print("Executed")  # can do anything here after calling the func1
    return now_exec  # iss function ko return kar dunga
# dec1 function now_exec function ko return karta hai

def who_is_vaibhav():
    print("vaibhav is a python programmer")

# who_is_vaibhav()

# line 52 and 53 is a decorator concept
who_is_vaibhav = dec1(who_is_vaibhav)  # ab jo func dec1 return karaigaa, who_is_vaibhav func uss kai equal ho jaiga, now who_is_vaibhav is equal to now_exec function.
who_is_vaibhav()

# another way of using the decorator concept is  @function_name
@ dec1      # this is the another way of writing line 52, just write this above the function.
def who_is_vaibhav():
    print("vaibhav is a python programmer")

who_is_vaibhav()

# HINT :--
# Jb ek hi kaam 10 function kai sath karna ho, toh sabsai badiya hai ki decorator ka concept use kar lo
# ek function bna lo of that work which is to be do in those 10 function and then iss function ko decorator ka concept use kar kai unn function-O- mai sandwiched kar doo

# ek function koi kaam kar rha ho and hum chatai hai ki uskai kuch kaam-O-kai beech ek yeh wala kaam ho, then we can use concept of decorator.

# Decorator - ek function ko dusrai function kai kaam-O-kai beech mai SAND-WICHED karna ho.