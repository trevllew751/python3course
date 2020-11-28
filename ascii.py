import pyfiglet
from termcolor import colored
from colorama import init

init()

msg = input("What would you like to print?\n")
color = input("What color?\n")
valid_colors = ("red", "green", "yellow" "blue", "magenta", "cyan", "grey")
if color not in valid_colors:
    color = "red"
ascii_art = colored(pyfiglet.figlet_format(msg), color=color, attrs=['blink'], on_color="on_green")
print(ascii_art)
