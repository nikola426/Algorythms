"""Сортировка выбором"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Предполагаем, что текущий элемент — минимальный
        min_index = i
        # Ищем минимальный элемент в оставшейся части массива
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами найденный минимальный элемент с первым элементом неотсортированной части
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Пример использования
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Отсортированный массив:", sorted_arr)
