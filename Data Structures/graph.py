class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        """Добавляет ребро между вершинами u и v."""
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # Неориентированный граф

    def bfs(self, start):
        """Обход в ширину (BFS) от стартовой вершины."""
        visited = set()
        queue = [start]
        vertexes = ''

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                vertexes += f'{vertex} '
                visited.add(vertex)
                queue.extend(neighbor for neighbor in self.adjacency_list[vertex] if neighbor not in visited)

        print(vertexes)

    def dfs(self, start):
        """Обход в глубину (DFS) от стартовой вершины."""
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        """Рекурсивная функция для обхода в глубину."""
        visited.add(vertex)
        print(vertex, end=' ')

        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)


# Пример использования
if __name__ == "__main__":
    g = Graph()
    edges = [
        (0, 1), (0, 2), (1, 3), (1, 4),
        (2, 5), (3, 6), (4, 6), (5, 6)
    ]

    for u, v in edges:
        g.add_edge(u, v)

    print("Обход в ширину (BFS):")
    g.bfs(0)  # Начинаем обход с вершины 0
    print("\nОбход в глубину (DFS):")
    g.dfs(0)  # Начинаем обход с вершины 0
