from turtle import right


def merge(list1, list2):
    """Takes two sorted list and combines them into one sorted list.
    Args:
        list1: sorted list 1
        list2: sorted list 2
    """
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    """Merge Sort

    Args:
        my_list (int): Sorts the given list via Merge Sort Algorithm

    Returns:
        list: Sorted List
    """
    if len(my_list) == 1:
        return my_list
    mid = len(my_list)//2
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


# list1 = [3, 54, 7, 9, 10, 111, 2, 5, 6, 8, 13, 12,  14, 15, 16]
# newlist = merge_sort(list1)
# print(newlist)
