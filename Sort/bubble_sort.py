"""Сортировка пузырьком"""

def bubble_sort(nums):
    n = len(nums)

    for j in range(n - 1):
        flag = False
        for index in range(n - 1 - j):
            if nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
                flag = True

        if not flag:
            break


arr = [2, -9, 87, 54, 0]

bubble_sort(arr)
print(arr)
