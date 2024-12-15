def median(arr):
    return kth_element(arr, len(arr) // 2)

def kth_element(arr, K):
    l, r = 0, len(arr) - 1

    while (l + 1) < r:
        pivot_index = partition(arr, l, r)

        if K >= pivot_index:
            l = pivot_index
        else:
            r = pivot_index - 1

    return arr[l]

def partition(arr, left, right):
    pivot = arr[right] # Выбираем последний элемент в качестве опорного
    i = left - 1  # Индекс меньшего элемента

    for j in range(left, right):
        if arr[j] < pivot:  # Если текущий элемент меньше опорного
            i += 1  # Увеличиваем индекс меньшего элемента
            arr[i], arr[j] = arr[j], arr[i]  # Обмениваем элементы

    # Перемещаем опорный элемент на правильную позицию
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1  # Возвращаем индекс опорного элемента


# Пример использования
nums = [-4, 0, 23, -9, -4, 77, 0, 33, -9]
print(kth_element(nums, 8))