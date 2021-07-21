# RELATED TOPICS:
# Hash Table | String | Design | Trie

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.patterns = collections.defaultdict(set)
        

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            for i in range(len(word)):
                self.patterns[word[:i]+"#"+word[i+1:]].add(word)
        
        
    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        for i in range(len(searchWord)):
            pattern = searchWord[:i]+"#"+searchWord[i+1:]
            if pattern in self.patterns:
                for word in self.patterns[pattern] :
                    if word != searchWord:
                        return True
        
        return False
        
