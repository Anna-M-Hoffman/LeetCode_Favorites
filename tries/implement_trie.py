# IMPLEMENT TRIE (PREFIX TREE)
# PrefixTree() Initializes the prefix tree object.
# void insert(String word) Inserts the string word into the prefix tree.
# boolean search(String word) Returns true if the string word is in the prefix tree, else false.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, else false.

class TrieNode:

    def __init__(self):
        self.child = {} # Nodes are in the form of hashmap because each node 
        # can have multiple children. A 1:Many relationship
        # Created like d = {'a': <TrieNode object>, 'b': <TrieNode object>}
        # Leaf node hashmaps are empty {}
        self.endOfWord = False # Node objects default attribute is False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() # Start the Trie with an empty node

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child: # Check whether char key exists in hashmap
                curr.child[char] = TrieNode()
            curr = curr.child[char] # Move to the child node for that character
        curr.endOfWord = True # Mark the node object endOfWord attribute as True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.child: # Checking for character in TrieNode()
                return False
            curr = curr.child[char] 
        return curr.endOfWord # True or false depending on prior setting when word was added

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.child:
                return False
            curr = curr.child[char]
        return True # endOfWord setting does not matter for prefixes
        





