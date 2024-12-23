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

    def split_child(self, parent, i):
        t = parent.t
        full_child = parent.children[i]
        new_child = BTreeNode(t, full_child.leaf)

        parent.children.insert(i + 1, new_child)  # Добавляем новый дочерний узел в родительский

        parent.keys.insert(i, full_child.keys[t - 1])  # Перемещаем средний ключ в родительский узел

        new_child.keys = full_child.keys[t:(2 * t - 1)]  # Ключи для нового дочернего узла

        if not full_child.leaf:  # Если не листовой узел
            new_child.children = full_child.children[t:(2 * t)]  # Перемещаем дочерние узлы

        full_child.keys = full_child.keys[0:(t - 1)]  # Оставшиеся ключи в полном дочернем узле

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
