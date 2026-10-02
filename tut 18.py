# Break and Continue statements --
# 1.CONTINUE
# jab hum continue statement likhati hai toh uskai neeche ka code nazar-aandaaz ho jata hai,jab tak given condition true rheti hai jab tak sirf
# continue statement kai upar ka code hi baar baar execute hota rheta hai,jaisai hi given comdition false hoti hai waise hi program loop sai bahar nikal kar(continue statement kai neeche walai)
# code ko execute start karnai lag jata hai

# 2.BREAK
# break statement reach hotai hi preogram loop sai bahar aa jaiga,means program loop sai exit lai laiga

# Thing to note --
# while(True) and while(1) -- ek aisa while loop hai jo "Hamesha" chalta hi rheta hai.

# i = 0
# while(True):
#     print(i + 1, end=" ")
#     if i == 44:
#         break # stop the loop
#     i = i + 1

# mai sirf uss number ko print karna chahta hu jo 5 sai bada hai
# i = 0
# while(True):    # WILL COME BACK TO HERE <<<----------- |
#     if i+1<5:                                        #  |
#         i = i +1                                     #  |
#         continue     # ------------------------------>> |
#
#     print(i + 1, end=" ")
#     if i == 44:
#         break # stop the loop
#     i = i + 1

# while():
#     while kai andar aa gai
# if(i == 44):
#     if kai andar aa gai

# QUIZ
# WAP to take input from user till number greater than 100 is enetered by the user.
# Way-1
# while(True):        # WILL COME BACK TO HERE <<<----------- |
#     num = int(input("Enter the number:"))               #   |
#     if num<=100:                                        #   |
#         continue         # ------------------------------>> |
#     print("Number entered is greater then 100")
#     break # stop the while loop

# Way-2
while(True):            # WILL COME BACK TO HERE <<<----------- |
    num = int(input("Enter the number:"))                    #  |
    if num>100:                                              #  |
        print("Number entered is greater then 100")          #  |
        break                                                #  |
    else:                                                    #  |
        continue     # -------------------------------------->> |



# while(True):
#     n = int(input("Enter the number: "))
#     if n>100:
#         print("Congratulations number is greater than hundred")
#         break
