class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        nums.sort()
        print(nums)

        longest = 1
        current = 1


        for i in range(len(nums)-1):
            if nums[i] + 1== nums[i + 1] :
                current  += 1
                longest = max(current, longest)
            elif nums[i] == nums[i+1]:
                continue
            else:
                current = 1

        return longest