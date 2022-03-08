# RELATED TOPICS
# Array | Math | Two Pointers

# not the simplest, but uses O(1) extra space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseList(list_, l, r):
            while l < r:
                list_[l], list_[r] = list_[r], list_[l]
                l += 1
                r -= 1
        
        n = len(nums)
        k %= n
        if k:
            nums.reverse()
            reverseList(nums, 0, k - 1)
            reverseList(nums, k, n - 1)
            
