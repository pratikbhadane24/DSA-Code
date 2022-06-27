def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


# arr = [19, 22, 3, 54, 5, 66, 17]
# sorted = insertion_sort(arr)
# print(sorted)  # [3, 5, 17, 19, 22, 54, 66]
