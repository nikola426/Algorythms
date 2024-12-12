"""Быстрая сортировка"""

def sort(left, right):
    main_index = left

    for index in range(left + 1, right + 1):
        if nums[index] < nums[main_index]:
            nums.insert(main_index, nums.pop(index))
            main_index += 1

    if left < (main_index - 1):
        sort(left, main_index - 1)

    if (main_index + 1) < right:
        sort(main_index + 1, right)


nums = [-4, 0, 23, -9, -4, 77, 0, 33, -9]

sort(0, len(nums) - 1)
print(nums)