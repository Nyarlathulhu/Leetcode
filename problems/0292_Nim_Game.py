# RELATED TOPICS:
# Math | Brainteaser | Game Theory

class Solution:
    def canWinNim(self, n: int) -> bool:
        # if I want to win, the number of stones left must be 1/2/3,
        # so this number earlier at the moment which my friend remove stones
        # MUST be 4
        # if I want to keep 4 stones left, there must be 5/6/7 stones when I
        # am taking them away
        # if there must be 5/6/7 stones left, then my friend have to choose
        # among 8 stones...
        # in conclusion, if there are 4-multiple stones left when it is my
        # turn, I DEFINITELY have the strategy to win: just keep the number
        # of the stones as 4 multiples
        # given that I go first, n MUST NOT be a 4 multiples
        return n % 4 != 0
    
