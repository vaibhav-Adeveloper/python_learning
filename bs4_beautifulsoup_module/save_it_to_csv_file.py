from bs4 import BeautifulSoup
# import requests
import csv


# code:
with open("sample.html", "r") as html_file:
    beatifulsoup_object = BeautifulSoup(html_file, 'lxml')

csv_file = open("csv_file", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Website Link'])

for article in beatifulsoup_object.find_all('div', class_="article"):
    headline = article.h1.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    website_link = article.find_all('a')[1].get('href')
    print(website_link)

    print()

    csv_writer.writerow([headline, summary, website_link])

csv_file.close()