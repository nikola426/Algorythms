def binary_search_recursive_by_AI(arr, target, left, right):
    if left > right:
        return -1  # Элемент не найден

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid  # Элемент найден
    elif arr[mid] < target:
        return binary_search_recursive_by_AI(arr, target, mid + 1, right)  # Ищем в правой половине
    else:
        return binary_search_recursive_by_AI(arr, target, left, mid - 1)  # Ищем в левой половине


nums = (-3, 0, 1, 4, 9, 23, 87, 98.9, 300)

index_by_AI = binary_search_recursive_by_AI(nums, 300, 0, len(nums) - 1)

print('Индекс:', index_by_AI)