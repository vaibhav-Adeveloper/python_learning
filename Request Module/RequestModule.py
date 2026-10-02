import requests

# GET request: means mai kisi bhi URL kai andar ghusi and uska content lai-aau.
# website - financial modelling prep .com - gives stock prices.
r = requests.get("https://financialmodelingprep.com/stable/search-symbol?query=AAPL&apikey=")
# r = requests.get("https://dogapi.dog/api/v2")
# r = requests.get("https://api.github.com/users")
print(r.text)
print(r.status_code)


# POST request:
# post request cache nhi hoti.

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":12,
#     "p3":234
# }
# r2 = requests.post(url=url, data=data)

# post request - ki ek api-endpoint hoti hai and uskai sath data bhejna padta hai.
# endpoint - URL

# Exercise:
# use any free api and give a post request and make a program.
