def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")

    return wrapper


@be_polite
def greet():
    print("My name is Nigseki.")


@be_polite
def rage():
    print("I HATE YOU!")


# we are decorating our function
# with politeness!
greet()
rage()
