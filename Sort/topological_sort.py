class Graph:
    def __init__(self, edges):
        self.adjacency_list = {}

        for u, v in edges:
            self.add_edge(u, v)

    def add_edge(self, u, v):
        """Добавляет ориентированное ребро от u к v."""
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)

    def topological_sort(self):
        """Выполняет топологическую сортировку графа."""
        visited = set()
        stack = []

        for vertex in self.adjacency_list:
            if vertex not in visited:
                self._topological_sort_util(vertex, visited, stack)

        return stack[::-1]  # Возвращаем в обратном порядке

    def _topological_sort_util(self, vertex, visited, stack):
        """Вспомогательная функция для обхода в глубину."""
        visited.add(vertex)

        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self._topological_sort_util(neighbor, visited, stack)

        stack.append(vertex)  # Добавляем вершину в стек после посещения всех соседей

# Пример использования
if __name__ == '__main__':
    edges = [
        (0, 1), (0, 2), (1, 3), (1, 4),
        (2, 5), (3, 6), (4, 6), (5, 6)
    ]
    g = Graph(edges)

    print("Топологическая сортировка:")
    print(g.topological_sort())
