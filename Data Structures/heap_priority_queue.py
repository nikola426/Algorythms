class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, priority, item):
        """Добавляет элемент с заданным приоритетом в очередь."""
        # Добавляем элемент в кучу
        self.heap.append((priority, item))
        self._bubble_up(len(self.heap) - 1)

    def remove(self):
        """Удаляет и возвращает элемент с наивысшим приоритетом."""
        if not self.heap:
            raise IndexError('remove from empty priority queue')

        # Сохраняем корень (наивысший приоритет)
        highest_priority_item = self.heap[0]

        # Перемещаем последний элемент в корень
        last_element = self.heap.pop()  # Удаляем последний элемент
        if self.heap:
            self.heap[0] = last_element  # Перемещаем его в корень
            self._bubble_down(0)  # Восстанавливаем свойства кучи

        return highest_priority_item[1]  # Возвращаем только элемент, без приоритета

    def _bubble_up(self, index):
        """Перемещает элемент вверх по куче для поддержания свойств кучи."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index][0] > self.heap[parent_index][0]:
            # Меняем местами текущий элемент и его родителя
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Рекурсивно поднимаем элемент вверх
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        """Перемещает элемент вниз по куче для поддержания свойств кучи."""
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # Проверяем левого ребенка
        if left_child_index < len(self.heap) and self.heap[left_child_index][0] > self.heap[largest][0]:
            largest = left_child_index

        # Проверяем правого ребенка
        if right_child_index < len(self.heap) and self.heap[right_child_index][0] > self.heap[largest][0]:
            largest = right_child_index

        # Если наибольший элемент не корень, меняем их местами и продолжаем вниз
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._bubble_down(largest)

    def is_empty(self):
        """Проверяет, пуста ли очередь."""
        return len(self.heap) == 0


# Пример использования
pq = PriorityQueue()
pq.insert(3, "task_low")
pq.insert(5, "task_high")
pq.insert(4, "task_medium")

while not pq.is_empty():
    print(pq.remove())  # Вывод: task_high, task_medium, task_low
