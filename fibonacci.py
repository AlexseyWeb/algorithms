""" Числа Фибоначи """

count_numbers = 15
first, second = 1, 1

print(first, second, end=" ")

for i in range(count_numbers-2):
    first, second = second, first + second
    print(second, end=" ")

print()
