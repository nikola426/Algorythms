class Node:
    def __init__(self, data):
        self.data = data  # Значение узла
        self.left = None  # Левый дочерний узел
        self.right = None  # Правый дочерний узел

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Корень дерева

    def insert(self, data):
        """Вставка нового узла в дерево."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        """Рекурсивная вставка."""
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right, data)

    def search(self, data):
        """Поиск узла с заданным значением."""
        return self._search_recursively(self.root, data)

    def _search_recursively(self, node, data):
        """Рекурсивный поиск."""
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursively(node.left, data)
        return self._search_recursively(node.right, data)

    def delete(self, data):
        """Удаление узла с заданным значением."""
        self.root = self._delete_recursively(self.root, data)

    def _delete_recursively(self, node, data):
        """Рекурсивное удаление."""
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursively(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursively(node.right, data)
        else:
            # Узел с одним потомком или без потомков
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Узел с двумя потомками: получить минимальный узел из правого поддерева
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data  # Заменяем значение
            node.right = self._delete_recursively(node.right, min_larger_node.data)  # Удаляем минимальный узел

        return node

    def _find_min(self, node):
        """Найти узел с минимальным значением."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """Обход дерева в симметричном порядке (inorder)."""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """Рекурсивный симметричный обход."""
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)

# Пример использования
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [10, 5, 15, 3, 7, 12, 18]

    for value in values:
        bst.insert(value)

    print("Симметричный обход:", bst.inorder_traversal())  # Вывод: [3, 5, 7, 10, 12, 15, 18]

    bst.delete(5)
    print("После удаления 5:", bst.inorder_traversal())  # Вывод: [3, 7, 10, 12, 15, 18]

    found_node = bst.search(15)
    print("Найден узел:", found_node.data if found_node else "Не найден")  # Вывод: Найден узел: 15
