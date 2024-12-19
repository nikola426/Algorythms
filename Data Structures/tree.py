from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

        # Времена входа и выхода
        self.time_in = None
        self.time_out = None

    def add_child(self, node):
        self.children.append(node)

class Tree:
    def __init__(self, root):
        self.root = root

    # Метод обхода в глубину
    def depth_first_search(self, node, visit_order):
        if node is None:
            return
        visit_order.append(node.value)  # Запоминаем порядок обхода
        for child in node.children:
            self.depth_first_search(child, visit_order)

    # Метод обхода в ширину
    def breadth_first_search(self, root):
        if root is None:
            return []

        visit_order = []

        # Используем двустороннюю очередь
        queue = deque([root])

        while queue:
            # Извлекаем из её начала ноду
            node = queue.popleft()

            # Добавляем значение ноды в список обхода
            visit_order.append(node.value)

            # Добавляем детей ноды в конец очереди
            queue.extend(node.children)

        return visit_order

    # Метод присвоения нодам времён входа и выхода
    def dfs_with_timing(self, node):
        global time
        if node is None:
            return

        time += 1
        node.time_in = time  # Время входа

        for child in node.children:
            self.dfs_with_timing(child)

        time += 1
        node.time_out = time  # Время выхода

    # Метод поиска пути к ноде
    def _find_path_to_node(self, root, path, k):
        if root is None:
            return False

        path.append(root.value)

        if root.value == k:
            return True

        for child in root.children:
            # Возвращаем True, если нода с нужным значением была найдена
            if self._find_path_to_node(child, path, k):
                return True

        # Если в поддереве ноды не находим нужную ноду, то перед выходом удаляем из списка значение той ноды, в которой
        # сейчас находимся и возвращаем False
        path.pop()
        return False

    # Метод поиска наименьшего общего предка для двух нод
    def find_lca(self, root, n1, n2):
        path1 = []
        path2 = []

        # Если хотя бы один путь не найден, то возвращаем None
        if not self._find_path_to_node(root, path1, n1) or not self._find_path_to_node(root, path2, n2):
            return None

        # Поэлементно сверяем пути. Как только элементы не равны, то возвращаем значение предыдущего элемента: это и
        # будет наименьший общий предок.
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1

        return path1[i - 1] if i > 0 else None


# Создание дерева
tree = Tree(TreeNode(1))
child_a = TreeNode(2)
child_b = TreeNode(3)
tree.root.add_child(child_a)
tree.root.add_child(child_b)
child_a.add_child(TreeNode(4))
child_a.add_child(TreeNode(5))
child_b.add_child(TreeNode(6))
child_b.add_child(TreeNode(7))

# Обходы
dfs_order = []
tree.depth_first_search(tree.root, dfs_order)
print("DFS Order:", dfs_order)

bfs_order = tree.breadth_first_search(tree.root)
print("BFS Order:", bfs_order)

# Времена входа и выхода
time = 0
tree.dfs_with_timing(tree.root)
print("Assignment of times completed. Root times:", tree.root.time_in, tree.root.time_out)

# Поиск LCA
lca = tree.find_lca(tree.root, 4, 5)
print("LCA of 4 and 5:", lca)

