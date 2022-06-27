def bubble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if my_list[i] < my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list


# arr = [19, 22, 3, 54, 5, 66, 17]
# sorted = bubble_sort(arr)
# print(sorted)  # [3, 5, 17, 19, 22, 54, 66]
