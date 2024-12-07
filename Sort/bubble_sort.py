def bubble_sort(nums):
    flag = True
    n = len(nums)

    while flag:
        flag = False

        for index in range(n - 1):
            if nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
                flag = True


arr = [2, -9, 87, 54, 0]

bubble_sort(arr)
print(arr)
