class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # inserts a word into the trie
        pass

    def search(self, word):
        # searches for a word in the trie
        pass

    def starts_with(self, prefix):
        # returns all words that start with the given prefix
        pass
