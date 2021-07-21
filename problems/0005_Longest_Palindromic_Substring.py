# RELATED TOPICS:
# String | Dynamic programming

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#'+'#'.join(s)+'#'
        pos = maxright = 0
        RL = [0]*len(s)
        maxcenter = 0
        
        for i in range(len(s)):
            if i<maxright:
                RL[i] = min(maxright-i, RL[pos*2-i] )
            else:
                RL[i] = 0
            while i-RL[i]-1>=0 and i+RL[i]+1<len(s) and s[i-RL[i]-1] == s[i+RL[i]+1]:
                RL[i] += 1
            if i+RL[i] > maxright:
                maxright = RL[i] + i
                pos = i
            if RL[i] > RL[maxcenter]:
                maxcenter = i
        return s[maxcenter-RL[maxcenter]:maxcenter+RL[maxcenter]+1].replace('#','')
    
