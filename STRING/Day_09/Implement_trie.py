class Trie:
    def __init__(self):
        self.words = set()
        self.prefixes = set()

    def insert(self, word):
        self.words.add(word)
        for i in range(1, len(word) + 1):
            self.prefixes.add(word[:i])

    def search(self, word):
        return word in self.words

    def startsWith(self, prefix):
        return prefix in self.prefixes
