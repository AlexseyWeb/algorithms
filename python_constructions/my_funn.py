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

def dict_to_list(dict_to_convert):
    list_for_convertion = []
    for key, value in dict_to_convert.items():
        if type(value) == int:
            value *= 2
        list_for_convertion.append((key, value))
    return list_for_convertion


print(dict_to_list({'a': 3, 'b': [], 'c': 100}))


def fillter_list(list_to_fillter, value_type):
    filtered_list = []
    for element in list_to_fillter:
        if type(element) == value_type:
            filtered_list.append(element)
    return filtered_list


print(fillter_list([35, True, 'abc', 10], int))
print(fillter_list([35, True, 'abc', 10], str))
print(fillter_list([35, True, 'abc', 10], bool))