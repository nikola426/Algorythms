class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.start = None
        self.end = None
        self.suffix_link = None


class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = SuffixTreeNode()
        self.build_suffix_tree()

    def build_suffix_tree(self):
        """Строит суффиксное дерево для заданной строки."""
        n = len(self.text)
        self.active_node = self.root
        self.active_edge = None
        self.active_length = 0
        self.remaining_suffix_count = 0
        self.last_new_node = None
        self.leaf_end = [-1]  # Используем список для изменения в методах

        for i in range(n):
            self.extend_suffix_tree(i)

    def extend_suffix_tree(self, pos):
        """Расширяет суффиксное дерево для символа в позиции pos."""
        self.leaf_end[0] += 1  # Увеличиваем конец листа
        self.remaining_suffix_count += 1
        self.last_new_node = None

        while self.remaining_suffix_count > 0:
            if self.active_length == 0:
                self.active_edge = pos  # Начинаем с текущего символа

            current_edge_char = self.text[self.active_edge]
            if current_edge_char not in self.active_node.children:
                # Если текущий символ не существует, создаем новый лист
                leaf_node = SuffixTreeNode()
                leaf_node.start = pos
                leaf_node.end = self.leaf_end[0]
                self.active_node.children[current_edge_char] = leaf_node

                if self.last_new_node is not None:
                    # Устанавливаем суффиксную ссылку
                    self.last_new_node.suffix_link = self.active_node

                self.last_new_node = None
            else:
                # Если текущий символ существует, идем по ребру
                next_node = self.active_node.children[current_edge_char]
                edge_length = next_node.end - next_node.start + 1

                if self.active_length >= edge_length:
                    # Переходим к следующему узлу
                    self.active_edge += edge_length
                    self.active_length -= edge_length
                    self.active_node = next_node
                    continue

                # Если текущий символ совпадает с символом на ребре
                if (self.text[next_node.start + self.active_length] ==
                        self.text[pos]):
                    # Увеличиваем длину активного ребра и выходим из цикла
                    if self.last_new_node is not None and \
                            self.active_node != self.root:
                        self.last_new_node.suffix_link = self.active_node

                    self.active_length += 1
                    break

                # Разделяем ребро и создаем новый узел
                split_node = SuffixTreeNode()
                split_node.start = next_node.start
                split_node.end = next_node.start + self.active_length - 1

                # Обновляем старый узел и создаем новый лист
                split_node.children[self.text[next_node.start +
                                              self.active_length]] = next_node

                next_node.start += self.active_length  # Сдвигаем старый узел

                split_node.children[self.text[pos]] = SuffixTreeNode()
                split_node.children[self.text[pos]].start = pos
                split_node.children[self.text[pos]].end = self.leaf_end[0]

                # Обновляем ссылки на детей и родителя
                self.active_node.children[current_edge_char] = split_node

                if self.last_new_node is not None:
                    # Устанавливаем суффиксную ссылку для предыдущего узла
                    self.last_new_node.suffix_link = split_node

                # Обновляем последний новый узел
                self.last_new_node = split_node

            # Уменьшаем количество оставшихся суффиксов для обработки
            self.remaining_suffix_count -= 1

            if self.active_node == self.root and \
                    self.active_length > 0:
                # Если мы достигли корня, перемещаем активный край и сбрасываем длину
                self.active_length -= 1
                self.active_edge = pos - (self.remaining_suffix_count - 1)
            elif self.active_node != self.root:
                # Переходим по суффиксной ссылке, если мы не в корне
                self.active_node = (self.last_new_node.suffix_link
                                    if self.last_new_node is not None else self.root)


# Пример использования:
text = "xabxac"
suffix_tree = SuffixTree(text)

# Здесь можно добавить методы для поиска подстрок или других операций.
