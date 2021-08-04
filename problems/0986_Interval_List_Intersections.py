# RELATED TOPICS:
# Array | Two Pointers

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            firstLeft, firstRight = firstList[i][0], firstList[i][1]
            secondLeft, secondRight = secondList[j][0], secondList[j][1]
            if secondRight >= firstLeft and firstRight >= secondLeft:
                ans.append([max(firstLeft, secondLeft), min(firstRight, secondRight)])
            if secondRight < firstRight:
                j += 1
            else:
                i += 1
        return ans
    
