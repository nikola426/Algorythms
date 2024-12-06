def rabin_karp_by_AI(text, pattern):
    """Поиск подстроки в строке с использованием алгоритма Рабина-Карпа."""
    n = len(text)
    m = len(pattern)
    base = 256  # Основание для хеширования (количество возможных символов)
    prime = 101  # Простое число для модуляции хеша

    # Вычисление хеша для шаблона и первого окна текста
    pattern_hash = 0
    text_hash = 0
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    # Сравнение хешей и проверка совпадений
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # Если хеши совпадают, проверяем символы
            if text[i:i + m] == pattern:
                print(f"Подстрока найдена на индексе {i}")

        # Вычисление хеша для следующего окна текста
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * (base ** (m - 1))) + ord(text[i + m])) % prime
            # Обработка отрицательного значения хеша
            if text_hash < 0:
                text_hash += prime

little_str = 'abdfggtuu'
big_str = 'aaaaabdfggtuuqqpp'

rabin_karp_by_AI(big_str, little_str)
