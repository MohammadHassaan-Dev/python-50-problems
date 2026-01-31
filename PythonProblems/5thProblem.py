def merge_two_list(list1, list2):
    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # agar list1 me elements reh gaye
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # agar list2 me elements reh gaye
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged


list1 = [1,2,4,9]
list2 = [1,3,4,10]
print(merge_two_list(list1, list2))
