# RELATED TOPICS:
# Array | Binary Search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchBound(tag):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if tag == "left":
                        right = mid - 1
                    elif tag == "right":
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            if tag == "left":
                if left >= len(nums) or nums[left] != target:
                    return -1
                return left
            elif tag == "right":
                if right < 0 or nums[right] != target:
                    return -1
                return right
        
        return [searchBound("left"), searchBound("right")]
    
