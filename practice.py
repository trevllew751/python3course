import pdb


# def is_odd_string(word):
#     yuh = dict(zip("abcdefghijklmnopqrstuvwxyz", range(1, 27)))
#     return all(yuh[s] % 2 == 1 for s in word)
#
# print(is_odd_string("a"))

# def reverse_vowels(word):
#     vowels = "aeiouAEIOU"
#     only_vowels = []
#     for letter in word:
#         if letter in vowels:
#             only_vowels.append(letter)
#     new_word = []
#     j = 0
#     for letter in word:
#         if letter in vowels:
#             new_word.append(only_vowels[-1-j])
#             j += 1
#         else:
#             new_word.append(letter)
#     return "".join(new_word)
#
#
#
#
# print(reverse_vowels("Hello!"))

# def three_odd_numbers(lst):
#     for i in range(0, len(lst) - 2):
#         if (lst[i] + lst[i+1] + lst[i+2]) % 2 == 1:
#             return True
#     return False
#
#
# print(three_odd_numbers([1, 2, 3, 4, 5])) #True
# print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])) #True
# print(three_odd_numbers([5, 2, 1])) #False
# print(three_odd_numbers([1, 2, 3, 3, 2])) #False

# def mode(lst):
#     counts = {}
#     for n in lst:
#         count = lst.count(n)
#         counts[count] = n
#     return counts.get(max(counts.keys()))
#
# print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4

# def letter_counter(string):
#     def counter(letter):
#         return string.lower().count(letter)
#     return counter
#
# counter2 = letter_counter('This Is Really Fun!')
# print(counter2('i'))
# print(counter2('t'))

# def running_average():
#     averages = []
#     def average(num):
#         averages.append(num)
#         return sum(averages)/len(averages)
#     return average
#
#
# rAvg = running_average()
# print(rAvg(10))# 10.0
# print(rAvg(11))# 10.5
# print(rAvg(12)) # 11
#
# rAvg2 = running_average()
# print(rAvg2(1))
# print(rAvg2(3))

# def once(fn):
#     def inner(num1, num2):
#         if not inner.has_run:
#             inner.has_run = True
#             return fn(num1, num2)
#         return None
#     inner.has_run = False
#     return inner
#
# def add(a,b):
#     return a+b
#
# oneAddition = once(add)
# print(oneAddition(2,2))
# print(oneAddition(2,2))
# print(oneAddition(12,200))

# def next_prime():
#     start = 2
#     while True:
#         if is_prime(start):
#             yield start
#         start += 1
#
# def is_prime(num):
#     if num == 2 or num == 3 or num == 5 or num == 7:
#         return True
#     return num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0
#
# primes = next_prime()
# print([next(primes) for i in range(25)])
