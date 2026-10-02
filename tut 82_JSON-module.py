# JSON - javaScript object notation
# yeh "data send/receive karnai ka ek tarika" hota hai, ek web protocol type ka hota hai.

import json

# about load & loads function.
data = '{"var1":"vaibhav", "var2":45, "var3":564}'
print(data)
# print(data['var1'])   # error will occur, because it is a string (data).
# parsing the above data
# string parsed into JSON.
parsed = json.loads(data)   # we converted the string into JSON data. now we can deal the data like of key-value pair.
# loads function parsed the data.
# string will get converted into python dictionary.
print(parsed)
print(parsed['var1'])   # no error will occur because the data is parsed.
print(parsed['var3'])
print(type(parsed))


# about dumps() function.

# python code ko javaScript compatible bananai kai liyai hum use kartai hai json.dumps()
# agar dictionary sai json banaigai, toh yeh error throw karaigaa.
# dumps() function python dictionary ko JSON string mai convert kar daigaa.

data2 = {
    "startup": "IoI solutions",
    "Investments": ['Stocks', 'Gold', 'Real Estate', 'Crypto'],
    "Organisations": ('LSPDS', 'IRIS'),
    "isBig": False
}

jscomp = json.dumps(data2)
print(jscomp)
print(type(jscomp))


# Task1 - json.load ?
# Task2 - what is sort_keys parameter in dumps().
