from queue import Queue


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Graph:
    def __init__(self, lab):
        self.N = len(lab)
        self.d = [[1000000 for _ in string] for string in lab]
        self.lab = [[sym for sym in string] for string in lab]
        self.q = Queue()
        self.dx = (1, 0, -1, 0)
        self.dy = (0, 1, 0, -1)

    def find_path(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.lab[i][j] == 'S':
                    self.d[i][j] = 0
                    self.q.put(Coord(i, j))

        while not self.q.empty():
            coord = self.q.get()
            x = coord.x
            y = coord.y

            for i in range(len(self.dx)):
                nx = x + self.dx[i]
                ny = y + self.dy[i]

                if self.is_inside(nx, ny):
                    if self.lab[nx][ny] == '.':
                        if self.d[nx][ny] == 1000000:
                            self.d[nx][ny] = self.d[x][y] + 1
                            self.q.put(Coord(nx, ny))
                    elif self.lab[nx][ny] == 'E':
                        print('Расстояние от старта до конца лабиринта:', self.d[x][y] + 1)

    def is_inside(self, x, y):
        if (0 <= x < self.N) and (0 <= y < self.N):
            return True

        return False


labirinth = [
    '#####E#',
    '##..#.#',
    '.##.#..',
    'S.....#',
    '.####.#',
    '......#',
    '#######'
]

g = Graph(labirinth)
g.find_path()
#N = len(labirinth)
