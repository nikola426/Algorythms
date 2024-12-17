"""Сортировка вставками"""

def insertion_sort(arr):
    # Проходим по всем элементам массива, начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]  # Текущий элемент для вставки
        j = i - 1

        # Перемещаем элементы arr[0..i-1], которые больше ключа, на одну позицию вперёд
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем ключ на правильное место
        arr[j + 1] = key

    return arr  # Возвращаем отсортированный массив


# Пример использования
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Отсортированный массив:", sorted_arr)