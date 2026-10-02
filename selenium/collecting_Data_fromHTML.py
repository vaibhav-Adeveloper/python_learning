from bs4 import BeautifulSoup
import os
import pandas as pd

dic = {"title": [], "price": [], "product_URL":[]}

for file_ in os.listdir("Data_"):
    try:
        with open(f"Data_/{file_}", encoding='utf-8') as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        # print(soup.prettify())

        # will write these html in csv file
        title = soup.find('div', class_="KzDlHZ").get_text()
        price = soup.find('div', attrs={"class": "Nx9bqj _4b5DiR"}).get_text()
        link = soup.find('a', class_="CGtC98")["href"]
        url_product = f"https://flipkart.com{link}"

        dic["title"].append(title)
        dic["price"].append(price)
        dic["product_URL"].append(url_product)
        # data = {"title": }

    except Exception as e:
        print(e)

df = pd.DataFrame(data=dic)
df.to_csv("data.csv", index=False, encoding='utf-8') 