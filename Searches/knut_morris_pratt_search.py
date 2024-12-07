def compute_prefix_function(pattern):
    """Вычисляет префикс-функцию для шаблона."""
    m = len(pattern)
    pi = [0] * m
    j = 0  # Длина предыдущего префикса

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]  # Переход к предыдущему префиксу
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j  # Записываем длину текущего префикса

    return pi

def knut_morris_pratt_by_AI(text, pattern):
    """Поиск подстроки с использованием алгоритма Кнута-Морриса-Пратта."""
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)  # Вычисляем префикс-функцию
    j = 0  # Индекс для шаблона

    for i in range(n):  # Проходим по тексту
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]  # Переход к предыдущему префиксу
        if text[i] == pattern[j]:
            j += 1
        if j == m:  # Найдено совпадение
            print(f"Подстрока найдена на индексе {i - m + 1}")
            j = pi[j - 1]  # Продолжаем поиск

pattern = 'abdfggtab'
text = 'abaaabdfggtabqqpp'

knut_morris_pratt_by_AI(text, pattern)
