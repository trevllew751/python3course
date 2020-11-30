# Custom for loop

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            nxt = next(iterator)
        except StopIteration:
            break
        else:
            func(nxt)

def square(x):
    print(x*x)

my_for([1,2,3,4], print)
my_for([1,2,3,4], square)