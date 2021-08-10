# RELATED TOPICS:
# Hash Table | String | Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = ans = 0
        window = {c: 0 for c in s}
        while right < len(s):
            char_in = s[right]
            window[char_in] += 1
            right += 1
            while window[char_in] > 1:
                char_out = s[left]
                left += 1
                window[char_out] -= 1
            ans = max(ans, right - left)
        return ans
    
