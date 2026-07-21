class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for num in nums:
            if num == target:
                return nums.index(num)
        else:
            return -1