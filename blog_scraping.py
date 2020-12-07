import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.rithmschool.com/blog"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blogdata.csv", "w", newline='') as file:
    csv_writer = writer(file)
    csv_writer.writerow(["title", "link", "date"])
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])

