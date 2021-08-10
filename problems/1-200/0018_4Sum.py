# RELATED TOPICS:
# Array | Two Pointers | Sorting

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums_sorted = sorted(nums)
        ans = []
        for fixed_pos1 in range(n - 3):
            if fixed_pos1 > 0 and \
               nums_sorted[fixed_pos1] == nums_sorted[fixed_pos1-1]:
                continue
            for fixed_pos2 in reversed(range(fixed_pos1 + 3, n)):
                if fixed_pos2 < n - 1 and \
                   nums_sorted[fixed_pos2] == nums_sorted[fixed_pos2+1]:
                    continue
                fix1 = nums_sorted[fixed_pos1]
                fix2 = nums_sorted[fixed_pos2]
                low = fixed_pos1 + 1
                high = fixed_pos2 - 1
                while low < high:
                    left = nums_sorted[low]
                    right = nums_sorted[high]
                    add_sum = left + right
                    if add_sum < target - fix1 - fix2:
                        while low < high and nums_sorted[low] == left:
                            low += 1
                    elif add_sum > target - fix1 - fix2:
                        while low < high and nums_sorted[high] == right:
                            high -= 1
                    else:
                        if [fix1, left, right, fix2] not in ans:
                            ans.append([fix1, left, right, fix2])
                        while low < high and nums_sorted[low] == left:
                            low += 1
                        while low < high and nums_sorted[high] == right:
                            high -= 1
        return ans
    
