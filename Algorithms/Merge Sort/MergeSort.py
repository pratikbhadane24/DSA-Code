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


# list1 = [1, 2, 5, 6, 8, 13]
# list2 = [3, 4, 7, 9, 10, 11, 12,  14, 15, 16]
# newlist = merge(list1, list2)
# print(newlist)
