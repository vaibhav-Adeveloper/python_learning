from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

elems = driver.find_elements(By.CLASS_NAME, "tUxRFH")
print(elems)  # return the list.

print(f"{len(elems)} elements found")
for elem in elems:
    print(elem.text)

# to get the html we will use outerHTML
# print(elem.get_attribute('outerHTML'))

# time.sleep(1)
driver.close()