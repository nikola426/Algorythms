class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Добавляет слово в бор."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_terminal = True  # Помечаем конец слова

    def search(self, word):
        """Ищет слово в бору. Возвращает True, если слово найдено."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_terminal  # Проверяем, является ли текущий узел терминальным

    def starts_with(self, prefix):
        """Проверяет, есть ли в боре слова с заданным префиксом."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Префикс найден

    def delete(self, word):
        """Удаляет слово из бора."""

        def _delete(node, word, depth):
            if not node:
                return False

            # Если мы достигли конца слова
            if depth == len(word):
                if not node.is_terminal:
                    return False  # Слово не найдено
                node.is_terminal = False  # Удаляем терминальность
                return len(node.children) == 0  # Возвращаем True, если нет детей

            char = word[depth]
            if char not in node.children:
                return False

            should_delete_current_node = _delete(node.children[char], word, depth + 1)

            if should_delete_current_node:
                del node.children[char]  # Удаляем ссылку на текущий символ
                return len(node.children) == 0  # Возвращаем True, если нет детей

            return False

        _delete(self.root, word, 0)


# Пример использования
trie = Trie()
words = ["apple", "app", "banana", "bat"]
for word in words:
    trie.insert(word)

print(trie.search("app"))  # Вывод: True
print(trie.search("appl"))  # Вывод: False
print(trie.starts_with("ban"))  # Вывод: True
trie.delete("app")
print(trie.search("app"))  # Вывод: False
