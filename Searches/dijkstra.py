import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        """Добавляет ориентированное ребро от u к v с заданным весом."""
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append((v, weight))  # (сосед, вес)

    def dijkstra(self, start):
        """Выполняет алгоритм Дейкстры и возвращает кратчайшие расстояния от начальной вершины."""
        # Инициализация
        distances = {vertex: float('infinity') for vertex in self.adjacency_list}
        distances[start] = 0
        priority_queue = [(0, start)]  # (расстояние, вершина)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Узел уже обработан с меньшим расстоянием
            if current_distance > distances[current_vertex]:
                continue

            # Обновляем расстояния до соседей
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight

                # Если найден более короткий путь к соседу
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Пример использования
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start_vertex = 'A'
    shortest_paths = g.dijkstra(start_vertex)

    print("Кратчайшие расстояния от вершины", start_vertex)
    for vertex, distance in shortest_paths.items():
        print(f"{start_vertex} -> {vertex}: {distance}")
