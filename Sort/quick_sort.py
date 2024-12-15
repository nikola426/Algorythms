"""
Оптимизировання быстрая сортировка со случайным выбором опорного элемента и меньшей глубиной рекурсии.
Больше всего подходит для больших массивов.
"""

from random import randint


def quicksort(arr, left, right):
    while left < right:
        pivot_index = randint(left, right)  # Случайный выбор опорного элемента
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # Перемещаем его в конец
        pivot_index = partition(arr, left, right)

        # Оптимизация: сортируем меньшую часть рекурсивно
        if pivot_index - left < right - pivot_index:
            quicksort(arr, left, pivot_index - 1)  # Сортируем левую часть
            left = pivot_index + 1  # Сортируем правую часть в цикле
        else:
            quicksort(arr, pivot_index + 1, right)  # Сортируем правую часть
            right = pivot_index - 1  # Сортируем левую часть в цикле


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
quicksort(nums, 0, len(nums) - 1)
print(nums)
