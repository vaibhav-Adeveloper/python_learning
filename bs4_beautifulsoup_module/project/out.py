string = input()
word_list = string.split()
string = ""
for word in word_list:
    word = word.capitalize()
    string += word + " "
print(string)

print(' '.join(word.capitalize() for word in input().split()))