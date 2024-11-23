from datetime import datetime


def log_functions_call(fn):
    """Function decorator

    Args:
        fn (*args, **kwargs): universal function for check arguments
    """
    def wrapper(*args, **kwargs):
        print(f"Function name {fn.__name__} ")
        print(f"Arguments {args} - {kwargs}")
        print(f"Call function {args} {kwargs} -> ", datetime.now())

        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Sorry TypeValidation {arg} {type(arg)}",
                                 "Arguments must be int and float!")

        result = fn(*args, **kwargs)
        return result
    return wrapper


@log_functions_call
def mul(first, second):
    return first * second


@log_functions_call
def sum_two_numbers(first, second):
    return first + second


try:
    mul_two_numbers = mul(22, 2)
    print(mul_two_numbers)

    print("-" * 30)

    sum_two = sum_two_numbers(first=[222, 22], second=333)
    print(sum_two)

    print("-" * 30)
    print(sum_two_numbers(first="22", second=323))

except Exception as e:
    print(e)


def decoration_func(original_func):
    def wrapper(*args, **kwargs):
        print("Before call my func")
        result = original_func(*args, **kwargs)
        total = sum(result)
        print(f"Sum your numbers: -> {total}")
        return result
    print("After call my func")
    return wrapper


@decoration_func
def info_output(first, second, third):
    print("This is a text!")
    return (first, second, third)


result = info_output(100, 50, 200)
print(result)
