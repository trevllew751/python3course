def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

print(sum(2, square))
print(sum(2, cube))