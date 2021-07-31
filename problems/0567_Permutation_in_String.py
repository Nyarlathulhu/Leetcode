# RELATED TOPICS:
# Hash Table | Two Pointers | String | Sliding Window

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = right = valid = 0
        window = {c: 0 for c in s1}
        count = {c: 0 for c in s1}
        for char in s1:
            count[char] += 1
        while right < len(s2):
            char_in = s2[right]
            right += 1
            if char_in in count:
                window[char_in] += 1
                if window[char_in] == count[char_in]:
                    valid += 1
            while right - left >= len(s1):
                if valid == len(count):
                    return True
                char_out = s2[left]
                left += 1
                if char_out in count:
                    if window[char_out] == count[char_out]:
                        valid -= 1
                    window[char_out] -= 1
        return False
    
