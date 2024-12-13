def permutations(arr):
    if len(arr) == 0:
        return [[]]  # Базовый случай: пустой список имеет одну перестановку — сам себя
    first_element = arr[0]
    rest = arr[1:]
    perms_without_first = permutations(rest)

    all_perms = []
    for perm in perms_without_first:
        for i in range(len(perm) + 1):
            # Вставляем первый элемент в каждую позицию в перестановках оставшихся элементов
            all_perms.append(perm[:i] + [first_element] + perm[i:])

    return all_perms


# Пример использования
arr = [1, 2, 3]
result = permutations(arr)
print("Все перестановки:", result)
