
# The SIH website loads content dynamically using JavaScript, which means requests + bs4 will NOT work because the HTML does not contain data directly.

# So we must use Selenium.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["sih_problems"]
collection = db["question"]

# Selenium Setup
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run browser in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.sih.gov.in/sih2025PS"
driver.get(url)
time.sleep(5)  # wait for JS to load

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

problems = soup.find_all("div", class_="problem_card")

for p in problems:
    title = p.find("h4").get_text(strip=True) if p.find("h4") else ""
    problem_id = p.find("span", class_="problem-code").get_text(strip=True) if p.find("span", class_="problem-code") else ""
    category = p.find("span", class_="cat_btn").get_text(strip=True) if p.find("span", class_="cat_btn") else ""
    domain = p.find("span", class_="theme_btn").get_text(strip=True) if p.find("span", class_="theme_btn") else ""
    ministry = p.find("span", class_="ministry_btn").get_text(strip=True) if p.find("span", class_="ministry_btn") else ""
    description = p.find("p").get_text(strip=True) if p.find("p") else ""

    # data = {
    #     "title": title,
    #     "category": category,
    #     "ministry": ministry,
    #     "description": description,
    #     "domain": domain,
    #     "problem_id": problem_id
    # }

    # collection.insert_one(data)

print("✅ Scraping Completed & Data Stored in MongoDB!")
