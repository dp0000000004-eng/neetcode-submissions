class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_number = float('inf')
        max_profit = 0


        for n in prices:
            if n < min_number:
                min_number = n
            elif n - min_number > max_profit:
                max_profit = n-min_number
        

        return max_profit