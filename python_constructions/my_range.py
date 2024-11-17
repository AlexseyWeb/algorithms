""" Working with range """


my_range = range(3, 20, 3)
my_second_range = range(100, 120)
another_range = list(my_range) + list(my_second_range)

print(my_second_range.count(10))
print(my_range.index(9))

convert_to_set = set(another_range)
print(convert_to_set)