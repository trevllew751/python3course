# def is_odd_string(word):
#     yuh = dict(zip("abcdefghijklmnopqrstuvwxyz", range(1, 27)))
#     return all(yuh[s] % 2 == 1 for s in word)
#
# print(is_odd_string("a"))

def reverse_vowels(word):
    vowels = "aeiou"
    indexes = {}
    for i in range(0, len(word)):
        if word[i] in vowels:
            indexes[word[i]] = i
    print(indexes)
    

reverse_vowels("Hello!")