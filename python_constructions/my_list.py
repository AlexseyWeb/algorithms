"""Working with list"""

number_list = [1, 2, 3, 4, 5, 6]
fruits_list = ['apple', 'banana', 'berry']

other_list = number_list.__add__(fruits_list)

for k, i in enumerate(other_list):
    merge_dict = {k:i}

print(merge_dict)
number_list.append(7)
number_list.pop(0)
# print(number_list)
# print(other_list)

