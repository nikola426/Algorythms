class Node:
    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Ссылка на следующий узел


class LinkedList:
    def __init__(self):
        self.head = None  # Указатель на первый узел

    def append(self, data):
        """Добавляет элемент в конец списка."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # Если список пуст, новый узел становится головой
            return
        current = self.head
        while current.next:  # Проходим до конца списка
            current = current.next
        current.next = new_node  # Присоединяем новый узел к последнему элементу

    def print_list(self):
        """Выводит элементы списка."""
        current = self.head
        while current:
            print(current.data, end=' ')  # Печатаем данные текущего узла
            current = current.next  # Переходим к следующему узлу
        print()  # Переход на новую строку

    def delete(self, key):
        """Удаляет элемент из списка по значению."""
        current = self.head

        if current and current.data == key:  # Если нужно удалить голову
            self.head = current.next  # Перемещаем голову на следующий узел
            current = None
            return

        prev = None
        while current and current.data != key:  # Ищем элемент для удаления
            prev = current
            current = current.next

        if not current:  # Если элемент не найден
            return

        prev.next = current.next  # Пропускаем удаляемый элемент
        current = None  # Удаляем элемент


# Создаем односвязный список и добавляем элементы
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

# Выводим элементы списка
print("Содержимое списка:")
llist.print_list()  # Ожидаемый вывод: 1 2 3 4

# Удаляем элемент и выводим снова
llist.delete(2)
print("После удаления элемента со значением 2:")
llist.print_list()  # Ожидаемый вывод: 1 3 4
