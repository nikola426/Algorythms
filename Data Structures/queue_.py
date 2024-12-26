"""Реализация очереди с помощью списка"""

class Q:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        """Добавляет элемент в конец очереди."""
        self.items.append(item)

    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди."""
        if self.is_empty():
            print("Очередь пуста")
            return None
        return self.items.pop(0)

    def size(self):
        """Возвращает количество элементов в очереди."""
        return len(self.items)

# Пример использования
q = Q()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Вывод: 1
print(q.size())     # Вывод: 1


"""Реализация очереди с помощью класса deque"""

from collections import deque

d = deque()

# Добавление элементов
d.append('task1')
d.append('task2')

# Удаление элемента
print(d.popleft())  # Вывод: 'task1'
print(len(d))       # Вывод: 1


"""Реализация очереди с помощью класса Queue"""
from queue import Queue

q = Queue()

# Добавление элементов
q.put('task1')
q.put('task2')

# Удаление элемента
print(q.get())  # Вывод: 'task1'
print(q.qsize())  # Вывод: 1

"""Каждый из этих методов имеет свои преимущества и недостатки. Использование списков проще, но менее эффективно для 
больших объемов данных. deque предлагает хорошую производительность и гибкость, тогда как queue.Queue подходит для 
многопоточных приложений. Выбор подходящего метода зависит от конкретных требований проекта."""