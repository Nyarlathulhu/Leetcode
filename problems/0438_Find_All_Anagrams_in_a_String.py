# RELATED TOPICS:
# Hash Table | String | Sliding Window

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = right = valid = 0
        window = {c: 0 for c in p}
        count = {c: 0 for c in p}
        ans = []
        for char in p:
            count[char] += 1
        while right < len(s):
            char_in = s[right]
            right += 1
            if char_in in count:
                window[char_in] += 1
                if window[char_in] == count[char_in]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(count):
                    ans += [left]
                char_out = s[left]
                left += 1
                if char_out in count:
                    if window[char_out] == count[char_out]:
                        valid -= 1
                    window[char_out] -= 1
        return ans
    
