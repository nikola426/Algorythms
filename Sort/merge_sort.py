def sort_by_AI(arr):
    """Сортировка слиянием."""
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        left_half = arr[:mid]  # Делим массив на левую половину
        right_half = arr[mid:]  # Делим массив на правую половину

        sort_by_AI(left_half)  # Рекурсивно сортируем левую половину
        sort_by_AI(right_half)  # Рекурсивно сортируем правую половину

        i = j = k = 0

        # Слияние отсортированных половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Проверка на оставшиеся элементы в левой половине
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Проверка на оставшиеся элементы в правой половине
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


nums_list = [-4, 0, 23, -9, -4, 77, 0, 33, -9]

sort_by_AI(nums_list)
print(nums_list)
