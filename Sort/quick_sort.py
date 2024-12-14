def quicksort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)  # Рекурсивно сортируем левую часть
        quicksort(arr, pivot_index + 1, right)  # Рекурсивно сортируем правую часть

def partition(arr, left, right):
    pivot = arr[right]  # Выбираем последний элемент в качестве опорного
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
quicksort(nums, 0, len(nums) - 1)
print(nums)
