""" Mutable objects """

number_list = [1, 2, 3, 4]
other_list = number_list

other_list.append(9)

print(f"Mutable object created everytime {number_list} -> {other_list} ")

""" To avoid changing objects, you need to use the copy method  shallow copy"""

another_list = number_list.copy()
another_list.append(100)

print(f"{number_list} -> {another_list}")