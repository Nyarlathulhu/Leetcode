# RELATED TOPICS:
# Array | Design | Binary Indexed Tree | Segment Tree

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.array = [0] * 2 * self.n
        for i in range(self.n, 2 * self.n):
            self.array[i] = nums[i-self.n]
        for j in reversed(range(self.n)):
            self.array[j] = self.array[2*j] + self.array[2*j+1]
        

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.array[index] = val
        while index > 0:
            left = right = index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            self.array[index//2] = self.array[left] + self.array[right]
            index //= 2
        

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        range_sum = 0
        while left <= right:
            if left % 2 == 1:
                range_sum += self.array[left]
                left += 1
            if right % 2 == 0:
                range_sum += self.array[right]
                right -= 1
            left //= 2
            right //= 2
        return range_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
