"""Сортировка подсчётом"""

def counting_sort(arr):
    if not arr:
        return arr

    # Находим минимальное и максимальное значение в массиве
    min_value = min(arr)
    max_value = max(arr)

    # Создаем массив для подсчета количества вхождений
    count_range = max_value - min_value + 1
    count = [0] * count_range

    # Подсчитываем количество вхождений каждого элемента
    for num in arr:
        count[num - min_value] += 1

    # Создаем отсортированный массив
    sorted_index = 0
    for i in range(count_range):
        while count[i] > 0:
            arr[sorted_index] = i + min_value
            sorted_index += 1
            count[i] -= 1

    return arr

# Пример использования
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Отсортированный массив:", sorted_arr)
