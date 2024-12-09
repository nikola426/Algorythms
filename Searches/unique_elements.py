def unique_elem_search(arr):
    uniq_arr = [arr[0]]

    for elem in arr:
        for el in uniq_arr:
            if elem == el:
                break
        else:
            uniq_arr.append(elem)

    return uniq_arr

def unique_elems_in_sorted_arr(arr):
    uniq_arr = []

    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            uniq_arr.append(arr[i])

    uniq_arr.append(arr[-1])

    return uniq_arr

nums = (23, 33, 33, 8)
sorted_nums = (0, 2, 4, 4, 7, 9, 9)

print(unique_elem_search(nums))
print(unique_elems_in_sorted_arr(sorted_nums))