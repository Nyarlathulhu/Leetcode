# RELATED TOPICS:
# Math | Brainteaser

import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # this is actually a process of factorization
        # since all bulbs are off at the beginning, it must be
        # switched for odd number of times to be on
        # consider 16 bulbs, the 16th bulb will be switched 5 times:
        # 1/2/4/8/16, all these integers are factors of 16
        # noting that the number of factors of N is not greater
        # than the square root of N, so the number of lighting
        # bulbs at last can be counted by this
        return int(math.sqrt(n))
    
