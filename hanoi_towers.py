def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Переместить диск 1 со стержня {source} на стержень {destination}")
        return

    # Переместить n-1 дисков со стержня source на auxiliary
    hanoi(n - 1, source, auxiliary, destination)

    # Переместить последний диск со стержня source на destination
    print(f"Переместить диск {n} со стержня {source} на стержень {destination}")

    # Переместить n-1 дисков со стержня auxiliary на destination
    hanoi(n - 1, auxiliary, destination, source)

# Пример использования
n = int(input("Введите количество дисков: "))
hanoi(n, 'A', 'B', 'C')  # A - исходный стержень, B - целевой, C - вспомогательный
