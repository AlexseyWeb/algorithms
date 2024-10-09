"""A simple algorithm FreezBuzz"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in list_of_numbers:
    if i % 15 == 0:
        print("FreezBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Freez")


