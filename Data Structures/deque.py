"""Реализация дека с помощью списка"""

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        """Добавляет элемент в начало дека."""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Добавляет элемент в конец дека."""
        self.items.append(item)

    def remove_front(self):
        """Удаляет и возвращает элемент из начала дека."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)

    def remove_rear(self):
        """Удаляет и возвращает элемент из конца дека."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()

    def size(self):
        """Возвращает количество элементов в деке."""
        return len(self.items)

# Пример использования
deque = Deque()
deque.add_rear(1)
deque.add_rear(2)
deque.add_front(0)
print(deque.remove_front())  # Вывод: 0
print(deque.size())           # Вывод: 2


"""Реализация дека с помощью класса deque"""

from collections import deque

# Создание дека
dq = deque()

# Добавление элементов
dq.append(1)       # Добавление в конец
dq.append(2)
dq.appendleft(0)   # Добавление в начало

# Удаление элементов
print(dq.popleft())  # Вывод: 0
print(dq.pop())      # Вывод: 2

# Проверка размера
print(len(dq))      # Вывод: 1


"""Реализация дека с помощью кольцевого буфера"""

class CircularDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.deque = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def add_front(self, item):
        if self.is_full():
            raise IndexError("Deque is full")
        self.head = (self.head - 1) % self.capacity
        self.deque[self.head] = item
        self.size += 1

    def add_rear(self, item):
        if self.is_full():
            raise IndexError("Deque is full")
        self.deque[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        item = self.deque[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        self.tail = (self.tail - 1) % self.capacity
        item = self.deque[self.tail]
        self.size -= 1
        return item

# Пример использования кольцевого дека
circular_deque = CircularDeque(5)
circular_deque.add_rear(1)
circular_deque.add_rear(2)
circular_deque.add_front(0)
print(circular_deque.remove_front())  # Вывод: 0
print(circular_deque.remove_rear())   # Вывод: 2

"""Выбор метода реализации дека зависит от требований к производительности и функциональности. Использование 
collections.deque является наиболее простым и эффективным способом для большинства случаев, тогда как реализация на 
основе кольцевого буфера может быть полезна в специфических сценариях, требующих контроля над памятью."""