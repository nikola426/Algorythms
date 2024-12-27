def rle_encode(data):
    """Сжимает данные с использованием алгоритма RLE."""
    if not data:
        return ""

    encoded = []
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(data[i - 1] + str(count))
            count = 1

    # Добавляем последний пробег
    encoded.append(data[-1] + str(count))

    return ''.join(encoded)

def rle_decode(encoded_data):
    """Восстанавливает данные из сжатого формата RLE."""
    decoded = []
    i = 0

    while i < len(encoded_data):
        char = encoded_data[i]
        i += 1
        count_str = ''

        # Читаем количество повторений
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count_str += encoded_data[i]
            i += 1

        count = int(count_str)
        decoded.append(char * count)

    return ''.join(decoded)

# Пример использования
if __name__ == "__main__":
    original_data = "AAAABBBCCDAA"
    print("Исходные данные:", original_data)

    compressed_data = rle_encode(original_data)
    print("Сжатые данные:", compressed_data)

    decompressed_data = rle_decode(compressed_data)
    print("Восстановленные данные:", decompressed_data)
