# RELATED TOPICS:
# Hash Table | String | Backtracking

from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if not digits:
            return []
        if len(digits) == 1:
            return mapping[digits]
        ans = mapping[digits[0]]
        i = 1
        while i < len(digits):
            ans = (''.join(letter) for letter in product(ans, mapping[digits[i]]))
            i += 1
        return ans
        
