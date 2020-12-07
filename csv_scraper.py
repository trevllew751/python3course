import requests
from bs4 import BeautifulSoup
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    next_url = "/page/1/"
    while next_url:
        response = requests.get(f"{BASE_URL}{next_url}").text
        soup = BeautifulSoup(response, "html.parser")
        for quote in soup.find_all(class_="quote"):
            all_quotes.append({"quote": quote.find(class_="text").get_text(),
                               "author": quote.find(class_="author").get_text(),
                               "bio": quote.find("a")["href"]})
        next_page = soup.find(class_="next")
        next_url = next_page.find("a")["href"] if next_page else None
    return all_quotes


def write_quotes(quotes):
    with open("quotes.csv", "w", newline='', encoding="utf-8") as file:
        headers = ("quote", "author", "bio")
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


quote_list = scrape_quotes()
write_quotes(quote_list)
