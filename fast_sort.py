"""Fast sorting """

def quicksort(my_array):
    if len(my_array) <= 1:
        return my_array
    pivot = my_array[len(my_array) // 2]
    left = [x for x in my_array if x < pivot]
    middle = [x for x in my_array if  x == pivot]
    right = [x for x in my_array if x > pivot]

    return quicksort(left) + middle + quicksort(right)

arr = [3, 6, 8, 10, 1, 2, 1]

print(quicksort(arr))
