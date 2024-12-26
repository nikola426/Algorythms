"""Обход несвязного графа"""

class Graph:
    def __init__(self, edges):
        self.adjacency_list = {}
        self.v_set = set()

        for u, v in edges:
            self.add_edge(u, v)
            self.v_set.add(u)
            self.v_set.add(v)

        self.c = [None] * len(self.v_set)

    def add_edge(self, u, v):
        """Добавляет ребро между вершинами u и v."""
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # Неориентированный граф

    def _dfs(self, v, component_id):
        print_str = f'{v}'
        for u in self.adjacency_list[v]:
            if self.c[u] is None:
                self.c[u] = component_id
                print_str += ' <-> ' + self._dfs(u, component_id)

        return print_str

    def dfs(self):
        component_id = 0
        for key in self.adjacency_list:
            if self.c[key] is None:
                self.c[key] = component_id
                print(self._dfs(key, component_id))
                component_id += 1

        print('Количество связных компонент:', component_id)


if __name__ == '__main__':
    edges = [
        (0, 1), (1, 2), (1, 3), (2, 3),
        (4, 5), (5, 6), (6, 7),
    ]
    g = Graph(edges)

    g.dfs()
