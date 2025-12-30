"""
LeetCode 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Approach: One Pass (Iterative / Greedy)
Time Complexity: O(n) 
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        cost = 0
        profit = 0 

        for i in range(1,len(prices)):
            cost = prices[i] - min_price
            profit = max(profit,cost)
            min_price = min(min_price,prices[i])

        return profit
        
