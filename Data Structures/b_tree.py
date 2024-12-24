class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Минимальная степень
        self.leaf = leaf  # True, если узел является листом
        self.keys = []  # Список ключей в узле
        self.children = []  # Список дочерних узлов


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)  # Создаем корень
        self.t = t  # Минимальная степень

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:  # Если корень полон
            new_root = BTreeNode(self.t, False)
            new_root.children.append(root)  # Старый корень становится дочерним
            self.split_child(new_root, 0)  # Разделяем старый корень
            self.root = new_root  # Обновляем корень
            self.insert_non_full(new_root, k)  # Вставляем новый ключ
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:  # Если узел является листом
            node.keys.append(0)  # Добавляем пустое место для нового ключа
            while i >= 0 and k < node.keys[i]:  # Находим позицию для нового ключа
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k  # Вставляем новый ключ
        else:  # Если не является листом
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:  # Если дочерний узел полон
                self.split_child(node, i)
                if k > node.keys[i]:  # Определяем, в какой дочерний узел вставить
                    i += 1
            self.insert_non_full(node.children[i], k)

    @staticmethod
    def split_child(parent, i):
        t = parent.t
        full_child = parent.children[i]
        new_child = BTreeNode(t, full_child.leaf)

        parent.children.insert(i + 1, new_child)  # Добавляем новый дочерний узел в родительский

        parent.keys.insert(i, full_child.keys[t - 1])  # Перемещаем средний ключ в родительский узел

        new_child.keys = full_child.keys[t:(2 * t - 1)]  # Ключи для нового дочернего узла

        if not full_child.leaf:  # Если не листовой узел
            new_child.children = full_child.children[t:(2 * t)]  # Перемещаем дочерние узлы

        full_child.keys = full_child.keys[0:(t - 1)]  # Оставшиеся ключи в полном дочернем узле

    def delete(self, k):
        """Удаляет ключ k из B-дерева."""
        if not self.root:
            print("Дерево пустое")
            return

        self.delete_key(self.root, k)

        # Если корень стал пустым после удаления
        if len(self.root.keys) == 0:
            if self.root.leaf:
                self.root = None
            else:
                self.root = self.root.children[0]

    def delete_key(self, node, k):
        """Удаляет ключ из вершины"""
        idx = self.find_key(node, k)

        # Если вершина - лист, то просто удаляем ключ. Иначе запускаем специальную функцию удаления из вершины.
        if idx < len(node.keys) and node.keys[idx] == k:
            if node.leaf:
                node.keys.pop(idx)
            else:
                self.delete_from_internal_node(node, idx)
        else:
            if node.leaf:
                print(f"Ключ {k} не найден")
                return

            # Если количество ключей в сыне недостаточно, то добавляем их
            if len(node.children[idx].keys) < self.t:
                self.fill(node, idx)

            if idx == len(node.keys) and idx > len(node.keys):
                self.delete_key(node.children[idx - 1], k)
            else:
                self.delete_key(node.children[idx], k)

    @staticmethod
    def find_key(node, k):
        """Возвращает индекс первого ключа больше или равного k."""
        idx = 0
        while idx < len(node.keys) and node.keys[idx] < k:
            idx += 1
        return idx

    def delete_from_internal_node(self, node, idx):
        """Удаляет ключ из вершины, не являющейся листом"""

        # Если количество ключей в сыне не меньше t, то находим максимальный ключ в поддереве и переносим его в ключи
        # вершины
        if len(node.children[idx].keys) >= self.t:
            predecessor_key = self.get_predecessor(node.children[idx])
            node.keys[idx] = predecessor_key
            self.delete_key(node.children[idx], predecessor_key)

        # Или если количество ключей в соседнем правом сыне не меньше t, то находим минимальный ключ и переносим его в ключи
        # вершины
        elif len(node.children[idx + 1].keys) >= self.t:
            successor_key = self.get_successor(node.children[idx + 1])
            node.keys[idx] = successor_key
            self.delete_key(node.children[idx + 1], successor_key)

        # Иначе объединяем этих двух сыновей
        else:
            self.merge_nodes(node, idx)

    @staticmethod
    def get_predecessor(node):
        """Находит максимальный ключ в поддереве."""
        current_node = node
        while not current_node.leaf:
            current_node = current_node.children[-1]
        return current_node.keys[-1]

    @staticmethod
    def get_successor(node):
        """Находит минимальный ключ в поддереве."""
        current_node = node
        while not current_node.leaf:
            current_node = current_node.children[0]
        return current_node.keys[0]

    def fill(self, parent_node, index):
        """Заполняет недостаточный дочерний узел."""

        # Если в соседнем левом поддереве достаточное количество ключей, то перебрасываем ключ от соседнего левого сына
        # к данному сыну
        if index != 0 and len(parent_node.children[index - 1].keys) >= self.t:
            self.borrow_from_prev(parent_node, index)

        # Если в соседнем правом поддереве достаточное количество ключей, то перебрасываем ключ от соседнего правого
        # сына к данному сыну
        elif index != len(parent_node.keys) and len(parent_node.children[index + 1].keys) >= self.t:
            self.borrow_from_next(parent_node, index)

        else:
            # Если ни у одного из соседей нет достаточного количества ключей, то объединяем двух его соседних сыновей
            if index != len(parent_node.keys):
                index_to_merge = index
            else:
                index_to_merge = index - 1

            self.merge_nodes(parent_node, index_to_merge)

    @staticmethod
    def borrow_from_prev(parent_node, index):
        """Перемещает ключ от соседнего левого сына к правому"""

        child_node = parent_node.children[index]
        sibling_node = parent_node.children[index - 1]

        # Объединяем ключи сына с родительским ключом
        child_node.keys.insert(0, parent_node.keys[index - 1])

        # Если сын не является листом, то объединяем его детей с крайним правым ребёнком соседнего левого сына
        if not child_node.leaf:
            child_node.children.insert(0, sibling_node.children.pop())

        # Меняем значение родительского ключа на значение самого правого ключа левого сына
        parent_node.keys[index - 1] = sibling_node.keys.pop()

    @staticmethod
    def borrow_from_next(parent_node, index):
        """Перемещает ключ от соседнего правого сына к левому"""

        child_node = parent_node.children[index]
        sibling_node = parent_node.children[index + 1]

        # Объединяем ключи сына с родительским ключом
        child_node.keys.append(parent_node.keys[index])

        # Если сын не является листом, то объединяем его детей с крайним левым ребёнком соседнего правого сына
        if not child_node.leaf:
            child_node.children.append(sibling_node.children.pop(0))

        # Меняем значение родительского ключа на значение самого левого ключа правого сына
        parent_node.keys[index] = sibling_node.keys.pop(0)

    @staticmethod
    def merge_nodes(parent_node, index):
        """Объединяет двух соседних сыновей"""

        left_child = parent_node.children[index]
        right_child = parent_node.children[index + 1]

        # Объединяем ключи левого сына с родительским ключом
        left_child.keys.append(parent_node.keys[index])

        # Объединяем ключи левого сына с ключами правого
        for key in right_child.keys:
            left_child.keys.append(key)

        # Если левый ребёнок не является листом, то объединяем детей левого ребёнка с детьми правого (объединяем
        # соседние поддеревья)
        if not left_child.leaf:
            for child in right_child.children:
                left_child.children.append(child)

        # Удаляем ссылку на правого ребёнка
        parent_node.children.pop(index + 1)

        parent_node.keys.pop(index)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        print("Level", level, ":", len(node.keys), "Keys:", node.keys)

        for child in node.children:
            self.print_tree(child, level + 1)


# Пример использования B-дерева
if __name__ == "__main__":
    b_tree = BTree(3)  # Создаем B-дерево с минимальной степенью t=3

    keys_to_insert = [10, 20, 5, 6, 12, 30]
    for key in keys_to_insert:
        b_tree.insert(key)

    print("Содержимое B-дерева:")
    b_tree.print_tree()

    b_tree.delete(6)

    print("Содержимое B-дерева:")
    b_tree.print_tree()
