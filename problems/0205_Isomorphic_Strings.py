# RELATED TOPICS
# Hash Table | String

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_2_t = {}
        t_2_s = {}
        
        for c1, c2 in zip(s, t):
            if c1 not in s_2_t and c2 not in t_2_s:
                s_2_t[c1] = c2
                t_2_s[c2] = c1
            elif s_2_t.get(c1) != c2 or t_2_s.get(c2) != c1:
                return False
        
        return True
    
