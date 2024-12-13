"""Сортировка слиянием"""

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


"""Сортировка слиянием с использованием буфера"""

def buf_sort(arr, left, right, buf):
    if (right - left) <= 1:
        return

    mid = (left + right) // 2

    buf_sort(arr, left, mid, buf)
    buf_sort(arr, mid, right, buf)
    merge(arr, left, mid, right, buf)

def merge(arr, l, m, r, buf):
    p1, p2 = l, m
    rp = 0

    while (p1 < m) or (p2 < r):
        if p1 == m:
            buf[rp] = arr[p2]
            rp += 1
            p2 += 1
            continue
        if p2 == r:
            buf[rp] = arr[p1]
            rp += 1
            p1 += 1
            continue
        if arr[p1] < arr[p2]:
            buf[rp] = arr[p1]
            rp += 1
            p1 += 1
        else:
            buf[rp] = arr[p2]
            rp += 1
            p2 += 1

    for i in range(l, r):
        arr[i] = buf[i - l]

def sort(arr):
    len_arr = len(arr)
    buf = [None] * len_arr

    buf_sort(arr, 0, len_arr, buf)


nums_list = [-4, 0, 23, -9, -4, 77, 0, 33, -9]

sort_by_AI(nums_list)
print(nums_list)

nums_list = [-4, 0, 23, -9, -4, 77, 0, 33, -9]

sort(nums_list)
print(nums_list)