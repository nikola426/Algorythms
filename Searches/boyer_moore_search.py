from timer import timer


def bm_preprocess(pattern):
    """Создает таблицу смещений для плохого символа."""
    bad_char_shift = {}
    pattern_length = len(pattern)

    for i in range(pattern_length):
        bad_char_shift[pattern[i]] = i

    return bad_char_shift

@timer
def boyer_moore(text, pattern):
    """Ищет вхождение подстроки (pattern) в строке (text) с помощью алгоритма Бойера-Мура."""
    bad_char_shift = bm_preprocess(pattern)
    text_length = len(text)
    pattern_length = len(pattern)

    i = 0  # индекс в тексте
    while i <= text_length - pattern_length:
        j = pattern_length - 1  # индекс в шаблоне

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:  # найдено совпадение
            print(f"Pattern found at index {i}")
            i += (pattern_length if i + pattern_length < text_length else 1)
        else:
            # Сдвиг по таблице плохого символа
            shift = bad_char_shift.get(text[i + j], -1)
            i += max(1, j - shift)


# Пример использования
text = 'aaaaabdfggtuuqqpp'
pattern = 'abdfggtuu'
boyer_moore(text, pattern)
