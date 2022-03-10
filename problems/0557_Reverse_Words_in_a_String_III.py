# RELATED TOPICS
# Two Pointers | String

# not the fastest
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        word_rev = []
        for word in words:
            alpha_list = list(word)
            l, r = 0, len(alpha_list) - 1
            while l < r:
                alpha_list[l], alpha_list[r] = alpha_list[r], alpha_list[l]
                l += 1
                r -= 1
            word_rev.append("".join(alpha_list))
        return " ".join(word_rev)
      
