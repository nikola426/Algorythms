"""Задача про словарь (алфавит):
Есть неизвестный язык инопланетян, который использует латинский
алфавит.
Порядок букв в нём может отличаться от обычного.
Например, быть «z, y, x, … a» или «c, a, e, h, p, b, x, y…».
Вам дан набор слов инопланетного языка, отсортированный
в лексикографическом порядке.
Восстановите порядок букв в алфавите инопланетян и выведите его.
Если возможных порядков несколько, выведите любой.
"""

from Sort.topological_sort import Graph


def create_alphabet(words):
    edges = []

    # Проходимся по словам в списке
    for i in range(len(words) - 1):

        # Находим наименьшую длину из длин двух соседних слов
        min_len = min(len(words[i]), len(words[i + 1]))

        # Сравниваем каждую букву слова с буквой следующего. Если буквы не равны, то, значит, в новом алфавите сначала
        # идёт буква первого слова, затем второго. Добавляем их в список рёбер в таком же порядке в качестве вершин
        # ориентированного графа.
        for j in range(min_len):
            if words[i][j] != words[i + 1][j]:
                edges.append((words[i][j], words[i + 1][j]))

    g = Graph(edges)

    # проводим топологическую сортировку графа и выводим на экран готовый алфавит
    print('Алфавит:', ''.join(g.topological_sort()))

sorted_words = [
    'wrt',
    'wrf'
    'er',
    'ett',
    'rftt'
]

create_alphabet(sorted_words)