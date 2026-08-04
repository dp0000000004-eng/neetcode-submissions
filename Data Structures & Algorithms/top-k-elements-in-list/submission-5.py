from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        ans = []

        for i in range(k):
            ans.append(count.most_common()[i][0])
        
        return ans