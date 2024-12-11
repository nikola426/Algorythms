# Стек представляет из себя односвязный список, в котором есть только команды "добавить" и "удалить" в конец списка, а
# также прочитать последний элемент.
# Здесь представлена реализация рекурсивной функции opt_pow из optimized_pow.py в виде стека. Это оптимизированная
# функция для возведения числа в целую положительную степень.

class Node:
    def __init__(self, a, b, pos):
        self.a = a  # Данные узла
        self.b = b
        self.pos = pos
        self.next = None  # Ссылка на следующий узел


class Stack:
    def __init__(self):
        self.head = None  # Указатель на первый узел

    def append(self, a, b, pos):
        """Добавляет элемент в конец стека"""
        new_node = Node(a, b, pos)

        if not self.head:
            self.head = new_node  # Если список пуст, новый узел становится головой
            return

        current = self.head

        while current.next:  # Проходим до конца списка
            current = current.next

        current.next = new_node  # Присоединяем новый узел к последнему элементу

    def peek(self):
        """Возвращает последний элемент стека"""

        if not self.head:
            print('Стек пуст! Невозможно прочитать последний элемент')
            return

        current = self.head

        while current.next:
            current = current.next  # Переходим к следующему узлу

        return current

    def pop(self):
        """Удаляет последний элемент из стека"""

        if not self.head:
            print('Стек пуст! Невозможно удалить последний элемент.')
            return

        current = self.head
        prev = None

        while current.next:
            prev = current
            current = current.next  # Переходим к следующему узлу

        if prev:
            current = None  # Удаляем последний элемент
            prev.next = None  # Удаляем ссылку на последний элемент
        else:
            self.head = None # Удаляем голову, если она осталась одна


def opt_pow_2(a, b):
    st = Stack()
    st.append(a, b, 0)
    ret = 0

    while st.head:
        a = st.peek().a
        b = st.peek().b
        pos = st.peek().pos
        st.pop()

        if pos == 0:
            if not b:
                ret = 1
            elif not (b % 2):
                st.append(a, b, 1)
                st.append(a, b / 2, 0)
            else:
                st.append(a, b, 2)
                st.append(a, b - 1, 0)
        elif pos == 1:
            ret *= ret
        else:
            ret *= a

    return ret

print(opt_pow_2(2, 4))
