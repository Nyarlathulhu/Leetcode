# RELATED TOPICS:
# Array | Two Pointers | Sorting

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 3:
            return []
        nums_sorted = sorted(nums)
        ans = []
        for fixed_pos in range(n - 2):
            fix = nums_sorted[fixed_pos]
            low = fixed_pos + 1
            high = n - 1
            while low < high:
                left = nums_sorted[low]
                right = nums_sorted[high]
                add_sum = left + right
                if add_sum < -fix:
                    while low < high and nums_sorted[low] == left:
                        low += 1
                elif add_sum > -fix:
                    while low < high and nums_sorted[high] == right:
                        high -= 1
                else:
                    if [fix, left, right] not in ans:
                        ans.append([fix, left, right])
                    while low < high and nums_sorted[low] == left:
                        low += 1
                    while low < high and nums_sorted[high] == right:
                        high -= 1
        return ans
    
