class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}
        ans = []

        for i, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                ans.append(i)
                ans.append(seen[comp])
            seen[num] = i

        ans.sort()

        for i in range(len(ans)):
            ans[i] = ans[i] + 1

        return ans
