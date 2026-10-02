from bs4 import BeautifulSoup
# import requests

# Web Scraping means to get the specific data from the website in the form of csv file or excel.

# we required the html parser along with the module - to parse our html of the website.
# html parser - lxml, html5lib etc.
# request library required to make get,post request to the website.

# steps:-
# 1. first we have to pass our html to beautifulsoup to get the beautifulsoup object.
# we can pass our html in the form of string or in the form of html file.


# code:
with open("sample.html", "r") as html_file:
    beatifulsoup_object = BeautifulSoup(html_file, 'lxml')

# print(beatifulsoup_object)
# to format the html - make the html display in formatted order/style.
# print(beatifulsoup_object.prettify())

# now let see how to grab information from this html.
# 1. how to get the tag information.
# html_title = beatifulsoup_object.title
# print(html_title)
html_title = beatifulsoup_object.title.text
# print(html_title)
# but thi swill get you the first title tag in html.
# but it is not necessary that only one title tag is there in the html, so to access the other same tag in html we have find() mwthod.


# for example there are so many div tag in the website, in our sample.html we have 3 div tag, but accessing it with the dot operator
# will just give you only first div tag in the html.
first_div_tag = beatifulsoup_object.div
# print(first_div_tag)

# so find() takes argument that which div tag we want, meaning give the div tag with this class or id.
# we don't use class, we use class_ in find() method because in python - class keyword is reserved for creating the classes (OOPS).
# find will give the first article,section,div etc.

footer_div = beatifulsoup_object.find('div', class_="footer")
# print(footer_div)

# now scrapping comes - we want all the articles and thier summary snippet.
article_div = beatifulsoup_object.find('div', class_="article")
# print(article_div)

# headline = article_div.h1.a.text
# print(headline)

# summary = article_div.p.text
# print(summary)

# above is the code to attain single div article - headline and summary.
# now to get the article and summary of all the div tag of class article -->

# we have a find_all() method.
# find_all() method returns a list containing all the div tags with the specified class.

for article in beatifulsoup_object.find_all('div', class_="article"):
    headline = article.h1.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    website_link = article.find_all('a')[1].get('href')
    print(website_link)

    print()