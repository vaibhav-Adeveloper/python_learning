# Else & Finally in Try Except.

f1 = open("vaibhav.txt", "rt")

try:
    f = open("does.txt")
    # f = open("vaibhav2.txt")

# except Exception as e:
#     print(e)
except EOFError as e:
    print("EOF error aa gya", e)
except IOError as e:
    print("IO error aa gya hai", e)

else:
    print("This will only run if except is not running")

finally:
    print("Run this anyway...")
    f1.close()
    # f.close()   # error isliyai aa rha hai ismai kyuki esi koi file exit nhi karti hai.

print("Important task is happening")

# agar mai aise cheez chahta hu karna ki chahaye code try block mai enter ho ya phir except block mai enter ho, yeh kaam toh hona hi hai,
# chahye error aai ya na aai, yeh kaam toh execute hona hi chaiye.
# in this scenerio we use --> finally

# agar except run hoga toh else run nhi hoga and if except run nhi hoga toh else run hoga.


# app ek sai zyada except statement bhi likh saktai hai, alag alag errors kai liyai.
