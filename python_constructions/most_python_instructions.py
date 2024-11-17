import timeit

#1 variant
first_variant = timeit.timeit("a, b = 10, 12; temp=b; a = temp")
print(first_variant)

#2 most speed variant
second_variant = timeit.timeit("a, b = 10, 12; a,b = b,a")
print(second_variant)