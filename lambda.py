# square2 = lambda num: num * num
#
# print(square2(7))

# nums = [2, 4, 6, 8, 10]
# doubles = map(lambda x: x*2, nums)
# for num in doubles:
#     print(num)

# people = ["Trevor", "Jason", "Derek", "Mom", "Dad"]
# peeps = map(lambda name: name.upper(), people)
# print(list(peeps))

# lst = [1, 2, 3, 4]
# evens = list(filter(lambda x: x % 2 == 0, lst))
# print(evens)

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# inactive_users = list(filter(lambda u: not u["tweets"], users))
# print(inactive_users)

# inactive_users = list(map(lambda user: "@" + user["username"], filter(lambda u: not u["tweets"], users)))
inactive_users = ["@" + u["username"] for u in users if not u["tweets"]]
print(inactive_users)
