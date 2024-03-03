class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word:str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search(self, word:str):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def delete(self, words):
        def delete_recurse(node, word, index):
            if len(word) == index:
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0

            char = word[index]
            if not node.children[char]:
                return False
            delete_node = delete_recurse(node.children[char], word, index+1)

            if delete_node:
                del node.children[char]
                return len(node.children) == 0
            return False

        delete_recurse(self.root, words, 0)

    def prefix_search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self.find_words(node, prefix)

    def find_words(self, node, prefix):
        words = []
        if node.is_end:
            words.append(prefix)
        for char,child in node.children.items():
            words.extend(self.find_words(child, prefix + char))
        return words


trie = Trie()
trie.insert('apple')
trie.insert('ape')
trie.insert('ant')
print(trie.search('apple'))
# print(trie.delete('ape'))
print(trie.search('ape'))
print(trie.search('appl'))
print(trie.prefix_search('ap'))
