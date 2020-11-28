from termcolor import colored
from colorama import init
init()
text = colored("hi there", color="cyan", on_color="on_yellow", attrs=["blink"])
print(text)

