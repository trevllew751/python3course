# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)


# Common PDB commands
# l (list)
# n (next line)
# p (print)
# C (continue = finishes debugging)

def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace()
    return a + b + c + d


add_numbers(1,2,3,4)


def divide(num1, num2):
    try:
        return num1/num2
    except TypeError:
        print("Please provide two integers or floats")
    except ZeroDivisionError:
        print("Please do not divide by zero")