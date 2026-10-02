from bs4 import BeautifulSoup
import requests

class BookScraper:
    base_url = "http://books.toscrape.com/"

    def __init__(self):
        self.categories = {}
        self.books = []

    def get_soup(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {url}")
        response.encoding = "utf-8"
        return BeautifulSoup(response.text, 'lxml')

    def fetch_categories(self):
        soup = self.get_soup(self.base_url)
        category_section = soup.find("ul", class_="nav nav-list").find("ul")
        for li in category_section.find_all("li"):
            name = li.get_text(strip=True)
            href = li.find("a")["href"]
            full_url = self.base_url + href
            # self.categories[name] = full_url
            self.categories.update({name: full_url})

    def handle_string(self, user_choice):
        return ' '.join(word.capitalize() for word in user_choice.split())

    def choose_category(self):
        print("List of all availaible categories of book available in website: books.toscrape.com \n")
        for index, categories in enumerate(self.categories.keys(), start=1):
            print(f"{index}). {categories}")
        print("\nEnter the category of book, which you are looking for: ", end="")
        user_choice = input()
        user_choice = self.handle_string(user_choice)
        return self.categories[user_choice]

    # category_url -  'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'

    def scrape_bookInfo(self, category_url):
        while True:
            soup = self.get_soup(category_url)
            book_items = soup.find_all("article", class_="product_pod")
            for book in book_items:
                name = book.h3.a['title']
                price = book.find('p', class_="price_color").text.strip()
                availability = book.find('p', class_="instock availability").get_text(strip=True)
                rating = book.p['class'][1]
                detail_partial_url = book.h3.a["href"].replace("../", "")
                detail_url = self.base_url + "catalogue/" + detail_partial_url
                detail_soup = self.get_soup(detail_url)
                available_qty = detail_soup.find('p', class_="instock availability").get_text(strip=True)
                next_page = soup.find("li", class_="next")
                # if next_page is not there then next_page will have its value None.
                if next_page:
                    next_page_url = next_page.a['href']
                # https://books.toscrape.com/catalogue/category/books/travel_2/index.html --> current page directory
                    category_url = category_url.rsplit("/", 1)[0] + "/" + next_page_url
                # after
                # https://books.toscrape.com/catalogue/category/books/travel_2/page-2.html --> next page directory

                    self.books.append({"BookName": name, "Price": price, "Rating": rating, "Quantity": available_qty})
                else:
                    break

            return self.books

    def display(self, book_list):
        print("Availaible information about the Book is: \n")
        print(f"Total {len(book_list)} Books of this Category are Available \n")
        for book_info in book_list:
            print(f"Book Name: {book_info['BookName']}")
            print(f"Book Price: {book_info['Price']}")
            print(f"Book Rating: {book_info['Rating']} out of Five")
            print(f"Book Quantity: {book_info['Quantity']}\n")


    def run(self):
        print("Welcome to Book Scraper\n")
        self.fetch_categories()
        category_url = self.choose_category()
        book_InfoList = self.scrape_bookInfo(category_url)
        self.display(book_InfoList)

# Main execution
if __name__=="__main__":
    scrapper = BookScraper()
    scrapper.run()