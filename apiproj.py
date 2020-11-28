import requests
from random import choice
from termcolor import colored
from colorama import init
from pyfiglet import figlet_format

init()
valid_colors = ("grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white")
colored_text = colored(figlet_format("Dad Joke 3000"), choice(valid_colors))
print(colored_text)

url = "https://icanhazdadjoke.com/search"
topic = input("Let me tell you a joke! Give me a topic: ")
response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params={"term": topic})
jokes_list = response.json()["results"]
if jokes_list:
    num_jokes = len(jokes_list)
    presentation = "Here's one:"
    joke_quantity = f"{num_jokes} jokes"
    if num_jokes == 1:
        presentation = "Here it is: "
        joke_quantity = "one joke"
    jokes = [x["joke"] for x in jokes_list]
    print(f"I've got {joke_quantity} jokes about {topic}. {presentation}")
    print(choice(jokes))
else:
    print(f"I've got no jokes about {topic}! Please try again.")
