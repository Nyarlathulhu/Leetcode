# RELATED TOPICS:
# Hash Table | String | Design | Trie

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = {}
        

    def insert(self, key: str, val: int) -> None:
        self.dictionary[key] = val
        

    def sum(self, prefix: str) -> int:
        addup = 0
        for k, v in self.dictionary.items():
            if k.startswith(prefix):
                addup += v
        return addup
        
