""" Working with functions """

# Callback functions


def some_func():
    print("some function")


def fn_call_func(callback):
    callback()


fn_call_func(some_func)

def greeting(greet):
    return lambda name: f"{greet} -> {name}"


x = greeting("Hello ")
print(x("Alexsey"))