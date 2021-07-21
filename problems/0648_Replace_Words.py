# RELATED TOPICS:
# Array | Hash Table | String | Trie

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary_sorted = sorted(dictionary, key=lambda x: len(x))
        words = sentence.split(' ')
        new_sentence = sentence
        for i in range(len(words)):
            for root in dictionary_sorted:
                if words[i].startswith(root):
                    words[i] = root
                    break
        
        new_sentence = ' '.join(words)
        return new_sentence
        
