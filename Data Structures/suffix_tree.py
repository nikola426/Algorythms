class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class SuffixTree:
    def __init__(self):
        self.root = SuffixTreeNode()

    def insert_suffix(self, suffix):
        """Добавляет суффикс в дерево."""
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]
        node.is_end_of_word = True  # Помечаем конец суффикса

    def build_suffix_tree(self, text):
        """Строит суффиксное дерево для заданной строки."""
        for i in range(len(text)):
            self.insert_suffix(text[i:])  # Добавляем каждый суффикс

    def search(self, pattern):
        """Ищет паттерн в суффиксном дереве."""
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Паттерн найден

# Пример использования
text = "banana"
suffix_tree = SuffixTree()
suffix_tree.build_suffix_tree(text)

# Проверка наличия подстрок
patterns = ["ana", "nan", "ban", "bat"]
for pattern in patterns:
    print(f"'{pattern}' найдено: {suffix_tree.search(pattern)}")
