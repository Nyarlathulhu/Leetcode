# RELATED TOPICS:
# Hash Table | String | Sliding Window

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = valid = start = 0
        sub_len = 100001
        window = {c: 0 for c in t}
        count = {c: 0 for c in t}
        for char in t:
            count[char] += 1
        while right < len(s):
            char_in = s[right]
            right += 1
            if char_in in count:
                window[char_in] += 1
                if window[char_in] == count[char_in]:
                    valid += 1
            while valid == len(count):
                if right - left < sub_len:
                    start = left
                    sub_len = right - left
                char_out = s[left]
                left += 1
                if char_out in count:
                    if window[char_out] == count[char_out]:
                        valid -= 1
                    window[char_out] -= 1
        return s[start:start+sub_len] if sub_len != 100001 else ""
    
