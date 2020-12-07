import requests
from bs4 import BeautifulSoup
from random import choice

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


# Game logic
def game(quotes):
    while True:
        guess_count = 4
        quote = choice(quotes)
        first_last = quote["author"].split(" ")
        url = f"{BASE_URL}{quote['bio']}"
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        birth = f'{soup.find(class_="author-born-date").get_text()} {soup.find(class_="author-born-location").get_text()}'
        hints = [f"The author was born {birth}.",
                 f"The author's first name starts with {first_last[0][0]}",
                 f"The author's last name starts with {first_last[1][0]}"]

        print(f"{quote['quote']}\nGuess the author of the quote")
        guess = input(f"You have {guess_count} guesses remaining. What is your guess? ")
        hint_num = 0
        ending = "Congrats!"
        while guess_count != 0:
            if guess.lower() != quote["author"].lower() and guess_count != 1:
                print("Wrong! Here's a hint:")
                print(hints[hint_num])
                hint_num += 1
                guess_count -= 1
                guess = input(f"You have {guess_count} guess(es) remaining. What is your guess? ")
            elif guess == quote["author"]:
                break
            else:
                ending = f"You ran out of guesses! The author was {quote['author']}."
                break
        play_again = input(f"{ending} Would you like to play again?(y/n) ")
        if play_again == 'y':
            game(quotes)
        else:
            break
    print("Thanks for playing!")


quotes = scrape_quotes()
game(quotes)
