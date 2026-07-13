class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        k = 0
        size = len(nums)
        
        for num in nums[k:]:
            if num == val:
                nums.remove(num)
                k += 1

        return size - k