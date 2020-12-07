import requests
from bs4 import BeautifulSoup
from random import randint

url = "http://quotes.toscrape.com/"
quotes = []
authors = []
bios = {}
while True:
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    for quote, author in zip(soup.find_all(class_="text"), soup.find_all(class_="author")):
        quotes.append(quote.text)
        authors.append(author.text)
    next_page = soup.find(class_="next")
    if not next_page:
        break
    next_url = next_page.findChild()["href"]
    url = f"http://quotes.toscrape.com{next_url}"

set_authors = set(authors)
for author in set_authors:
    first_last = author.split(" ")
    about_url = f"http://quotes.toscrape.com/author/{first_last[0]}-{first_last[1]}/"
    bio_soup = BeautifulSoup(requests.get(about_url).text, "html.parser")
    bios[author] = f"{bio_soup.find(class_='author-born-date').text} {bio_soup.find(class_='author-born-location').text}"

guess_count = 4
while True:
    index = randint(0, len(quotes) - 1)
    quote = quotes[index]
    author = authors[index]
    hints = [f"The author was born {bios[author]}",
             f"The author's first name starts with {author[0]}",
             f"The author's last name starts with {author.split(' ')[1][0]}"]
    hint_num = 0
    print(f"{quote}\nGuess the author of the quote")
    guess = input(f"You have {guess_count} guesses remaining. What is your guess? ")
    ending = "Congrats!"
    while guess_count != 0:
        if guess != author and guess_count != 1:
            print("Wrong! Here's a hint:")
            print(hints[hint_num])
            hint_num += 1
            guess_count -= 1
            guess = input(f"You have {guess_count} guess(es) remaining. What is your guess? ")
        elif guess == author:
            break
        else:
            ending = f"You ran out of guesses! The author was {author}."
            break
    play_again = input(f"{ending} Would you like to play again?(y/n) ")
    if play_again != 'y':
        break
    guess_count = 4
print("Thanks for playing!")
