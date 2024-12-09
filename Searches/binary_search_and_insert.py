def bin_search_and_insert(sorted_arr, num):
    left = 0
    right = len(sorted_arr) - 1

    while left < right:
        middle = (left + right) // 2

        if sorted_arr[middle] < num:
            left = middle + 1
        else:
            right = middle

    return left

sorted_nums = [-2, 0, 2, 2, 8]
sorted_nums.insert(bin_search_and_insert(sorted_nums, 7), 7)
sorted_nums.insert(bin_search_and_insert(sorted_nums, 7), 7)

print(sorted_nums)
