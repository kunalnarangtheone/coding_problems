from trie_node import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, char):
        current_node = self.root
        for c in char:
            children = current_node.children[c]

            else:
                node = self.root



        # if char not in self.root.children:
        #     self.root.children[char] = None
        #
        # else:
        #     children = self.root.children[char]
        #     while not children:
        #         children = children[]
