# d = {"name": "Ricky"}
#
#
# def get(di, key):
#     try:
#         return di[key]
#     except KeyError:
#         return None
#
#
# print(get(d, "gayseki"))
# print(get(d, "name"))

# while True:
#     try:
#         num = int(input("Please enter a number: "))
#     except ValueError:
#         print("Must enter a number")
#     else:
#         print("Nice number")
#         break
#     finally:
#         print("Runs no matter what")
# print("Rest of game logic")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except TypeError:
        print("a and b must be numeric types")
    else:
        print(f"The result of the division is {result}")


print(divide(1, 2))
print(divide(1, 0))
print(divide("a", 2))
