from functools import wraps


def log_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        print(f"You are about to call {function.__name__}")
        print(f"Here's the documentation: {function.__doc__}")
        return function(*args, **kwargs)

    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together"""
    return x + y


print(add(1, 2))
