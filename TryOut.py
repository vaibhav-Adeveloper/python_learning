book = ['1).Macbeth\n', '2).lovely\n']
print(book)


book = list(map(str.strip, book))
print(book)

c = list(filter(str.strip, book))
print(c)