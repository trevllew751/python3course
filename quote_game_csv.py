import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"


def read_quotes():
    with open("quotes.csv", encoding="utf-8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


# Game logic
def game(quotes):
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
    play_again = ""
    while play_again.lower() not in ('y', 'yes', 'n', 'no'):
        play_again = input(f"{ending} Would you like to play again?(y/n) ")
    if play_again.lower() in ('y', 'yes'):
        return game(quotes)
    print("Thanks for playing!")


game(read_quotes())
