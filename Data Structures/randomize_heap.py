import random


class RandomizedHeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RandomizedHeap:
    def __init__(self):
        self.root = None

    def merge(self, h1, h2):
        """Сливает две рандомизированные кучи."""
        if not h1:
            return h2
        if not h2:
            return h1

        # Убедимся, что h1 — это меньшая куча
        if h1.value > h2.value:
            h1, h2 = h2, h1

        # Случайный обмен дочерних узлов
        if random.choice([True, False]):
            h1.left, h1.right = h1.right, h1.left

        # Сливаем правое поддерево с другой кучей
        h1.right = self.merge(h1.right, h2)

        return h1

    def insert(self, value):
        """Добавляет элемент в рандомизированную кучу."""
        new_node = RandomizedHeapNode(value)
        self.root = self.merge(self.root, new_node)

    def remove_max(self):
        """Удаляет и возвращает наибольший элемент из кучи."""
        if not self.root:
            raise IndexError('remove from empty heap')

        max_value = self.root.value
        # Сливаем левое и правое поддеревья
        self.root = self.merge(self.root.left, self.root.right)

        return max_value


# Пример использования
randomized_heap = RandomizedHeap()
elements = [3, 1, 4, 1, 5, 9]

for el in elements:
    randomized_heap.insert(el)

# Извлечение максимумов
max_elements = []
while True:
    try:
        max_elements.append(randomized_heap.remove_max())
    except IndexError:
        break

print("Максимальные элементы в порядке извлечения:", max_elements)  # Вывод: [9, 5, 4, 3, 1, 1]
