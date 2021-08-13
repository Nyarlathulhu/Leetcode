# RELATED TOPICS:
# Array | Math | Dynamic Programming | Game Theory

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # in fact, Alice can ALWAYS pick either all odd-indexed piles
        # or all even-indexed piles of stones away, so what Alice only
        # needs to do is to find out which of them has the bigger total
        # amount of stones
        # in this way, Alice will ALWAYS win
        return True
    
