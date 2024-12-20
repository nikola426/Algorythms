class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        """Добавляет элемент в кучу."""
        self.heap.append(element)
        self._bubble_up(len(self.heap) - 1)

    def remove(self):
        """Удаляет и возвращает наименьший элемент из кучи."""
        if not self.heap:
            raise IndexError('remove from empty heap')

        # Сохраняем корень (наименьший элемент)
        min_element = self.heap[0]

        # Перемещаем последний элемент в корень
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self._bubble_down(0)

        return min_element

    def merge(self, other_heap):
        """Сливает текущую кучу с другой кучей."""
        for element in other_heap.heap:
            self.insert(element)

    def _bubble_up(self, index):
        """Вспомогательный метод для перемещения элемента вверх по куче."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            # Меняем местами текущий элемент и его родителя
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Рекурсивно поднимаем элемент вверх
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        """Вспомогательный метод для перемещения элемента вниз по куче."""
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # Проверяем левого ребенка
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        # Проверяем правого ребенка
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        # Если наименьший элемент не корень, меняем их местами и продолжаем вниз
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def is_empty(self):
        """Проверяет, пуста ли куча."""
        return len(self.heap) == 0

    def size(self):
        """Возвращает количество элементов в куче."""
        return len(self.heap)


# Пример использования
heap1 = MinHeap()
heap1.insert(5)
heap1.insert(3)
heap1.insert(8)

heap2 = MinHeap()
heap2.insert(7)
heap2.insert(2)

# Слияние куч
heap1.merge(heap2)

# Проверка элементов после слияния
removed_elements = []
while not heap1.is_empty():
    removed_elements.append(heap1.remove())

print(removed_elements)  # Вывод: [2, 3, 5, 7, 8]
