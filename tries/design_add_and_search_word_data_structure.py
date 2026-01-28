# DESIGN ADD AND SEARCH WORD DATA STRUCTURE
# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any string in the data structure that matches word
#  or false otherwise. word may contain dots '.' where dots can be matched with any letter.

class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root # self.root would wipe the recursion state
            for i in range(j, len(word)):
                # j takes the place of i as i+1 means dfs may be called within recursion 
                # and to be efficienct, j is marked further along 
                c = word[i]
                if c == ".": # Have to check all children
                    for child in curr.children.values():
                        if dfs(i + 1, child): # Recurse inside branch of tree
                            return True # If true, return true, else try another child branch
                            # If the recursion returns true, return True here
                    return False # Pattern not found in any of the children

                else:
                    if c not in curr.children:
                        return False # Letter (not dot) was not found in branch. No alternative branches can be checked.
                curr = curr.children[c] # Continue searching branches
            return curr.endOfWord # True or false depending if the finished search is marked as the end of the word
        
        return dfs(0, self.root)




        
