from random import choice

def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(("hahaha", "lol", "hehehe"))
        return f"{laugh} {person}"
    return get_laugh()

print(make_laugh_at_func("nigseki"))