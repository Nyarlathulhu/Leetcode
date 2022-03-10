# RELATED TOPICS
# Array | Two Pointers | Binary Search

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            addi = numbers[l] + numbers[r]
            if addi == target:
                return [l + 1, r + 1]
            elif addi < target:
                l += 1
            else:
                r -= 1
                
