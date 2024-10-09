def buble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(i):
            if int(my_list[j]) > int(my_list[j+1]):
                my_list[j],my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


new_list = buble_sort([1,7, 2, 3, 8, 11])
print(new_list)