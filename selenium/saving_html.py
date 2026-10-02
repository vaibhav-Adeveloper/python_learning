# getting the html page of the laptops in flipkart and saving these html in Data_ folder.
# now we can extract data from these scrappes html files like -- laptop_name, price, rating

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# import os
# list_ = os.listdir("./Data_")
# for item in list_ :
    # os.rename(f"Data_/{item}", f"Data_/{item}.html")
    # os.remove(f"Data_/{item}")

driver = webdriver.Chrome()
query = "laptop"
files = 0

for i in range(1, 8):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")

    elems = driver.find_elements(By.CLASS_NAME, "tUxRFH")
    # print(elems)  # return the list.

    print(f"{len(elems)} elements found", end="\n\n")

    for elem in elems:
        with open(f"Data_/{query}_{files}.html", "w", encoding="utf-8") as f:
            data = elem.get_attribute("outerHTML")
            f.write(data);
            files += 1

    # to get the html we will use outerHTML with get_attribute()
    # print(elem.get_attribute('outerHTML'))

    # time.sleep(1)

driver.close()