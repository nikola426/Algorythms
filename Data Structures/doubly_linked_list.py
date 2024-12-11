class Node:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.prev = None    # Ссылка на предыдущий узел
        self.next = None    # Ссылка на следующий узел

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Указатель на первый узел
        self.tail = None  # Указатель на последний узел

    def append(self, value):
        """Добавляет новый узел в конец списка."""
        new_node = Node(value)
        if not self.head:  # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Предыдущий последний узел указывает на новый
            new_node.prev = self.tail   # Новый узел ссылается на предыдущий последний узел
            self.tail = new_node        # Обновляем указатель tail

    def prepend(self, value):
        """Добавляет новый узел в начало списка."""
        new_node = Node(value)
        if not self.head:  # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Новый узел указывает на текущую голову
            self.head.prev = new_node   # Текущая голова ссылается на новый узел
            self.head = new_node        # Обновляем указатель head

    def display(self):
        """Выводит элементы списка от головы до хвоста."""
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def remove(self, value):
        """Удаляет первый найденный узел с указанным значением."""
        current = self.head
        while current:
            if current.value == value:
                if current.prev:  # Если это не голова
                    current.prev.next = current.next
                if current.next:  # Если это не хвост
                    current.next.prev = current.prev
                if current == self.head:  # Если это голова
                    self.head = current.next
                if current == self.tail:  # Если это хвост
                    self.tail = current.prev
                return  # Выход из функции после удаления узла
            current = current.next

# Пример использования:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.prepend(0)
dll.display()  # Вывод: 0 <-> 1 <-> 2 <-> None

dll.remove(1)
dll.display()  # Вывод: 0 <-> 2 <-> None
