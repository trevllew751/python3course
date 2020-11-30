from random import choice

def greet(person):
    def get_mood():
        return choice(("Hello there ", "Go away ", "I love you "))

    result = get_mood() + person
    return result

print(greet("nigseki"))