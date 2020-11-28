import random


# def sing_happy_birthday(name):
#     print("Happy Birthday to You")
#     print("Happy Birthday to You")
#     print(f"Happy Birthday Dear {name}")
#     print("Happy Birthday to You")
#
#
# sing_happy_birthday("Alex")

# def square(num):
#     return int(num) ** 2
#
#
# print(square(8))
# print(square(2))

# def flip_coin():
#     if random.random() > 0.5:
#         return "Heads"
#     else:
#         return "Tails"
#
#
# print(flip_coin())

# def print_full_name(first_name, last_name):
#     return f"{first_name} {last_name}"
#
#
# print(print_full_name("Trevor", "Lew"))


# def is_even(num):
#     return num % 2 == 0
#
#
# print(is_even(2))
# print(is_even(1))

# def exponent(num, power=2):
#     return num ** power

def list_manipulation(lst, command, location, value=None):
    locations = {"end": -1, "beginning": 0}
    if command == "remove":
        return lst.pop(locations.get(location))
    elif location == "end":
        lst.append(value)
    else:
        lst.insert(locations.get(location), value)
    return lst


print(list_manipulation([1,2,3], "add", "beginning", 20))

