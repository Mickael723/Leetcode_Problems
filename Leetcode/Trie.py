class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr_node = self.root

        for i in range(len(word)):

            letter_index = ord(word[i]) - ord('a')

            if curr_node.children[letter_index] is None:
                new_node = TrieNode()
                curr_node.children[letter_index] = new_node
            
            curr_node = curr_node.children[letter_index]

            if i == len(word) - 1:
                curr_node.isEndOfWord = True
        

    def search(self, word: str) -> bool:

        curr_node = self.root

        for i in range(len(word)):
            letter_index = ord(word[i]) - ord('a')

            if curr_node.children[letter_index] is None:
                return False
            
            elif i == len(word) - 1 and curr_node.children[letter_index].isEndOfWord:
                return True

            curr_node = curr_node.children[letter_index]

        return False

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for i in range(len(prefix)):
            letter_index = ord(prefix[i]) - ord('a')

            if curr_node.children[letter_index] is None:
                return False

            curr_node = curr_node.children[letter_index]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("bat")

    print(trie.search("apple"))   # Expected: True
    print(trie.search("app"))     # Expected: True
    print(trie.search("appl"))    # Expected: False
    print(trie.startsWith("app")) # Expected: True
    print(trie.startsWith("bat")) # Expected: True
    print(trie.startsWith("ba"))  # Expected: True

