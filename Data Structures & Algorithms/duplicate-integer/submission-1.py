class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        k = 1
        ans = False

        for i in range(len(nums)):
            try:
                if nums[i] == nums[k]:
                    ans = True
            
                else:
                    k += 1
            except IndexError:
                ans  = False
        
        return ans
        
            