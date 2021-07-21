# Prefix Tree
# RELATED TOPICS:
# Hash Table | String | Design | Trie

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ls = []
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.ls.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.ls:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for word in self.ls:
            if word.startswith(prefix):
                return True
        
        return False
        
