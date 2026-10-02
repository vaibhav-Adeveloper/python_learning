# Create the dictionary and take input from the user and return the meaning of the word from the dictionary
dict = {"Mutable":"Things can change","Immutable":"Things cannot change","Skycrapper":"Tall/High building","Desperation":"Sorrow,Last chance,Urgent",
        "Paranoia":"Suspicious,conspiracy,suspect"}
# print(dict)
# print(dict["Paranoia"])

# print("Enter the word:")
# word = input()
# print("Meaning of the word is:",dict[word])

# word = input("Enter the word:")
# print("Meaning of the word is:",dict[word])

word = input("Enter the word: ")
word = word.capitalize()
# print("Meaning of the word is:", dict[word])

print("Meaning of the word is: ", dict.get(word))