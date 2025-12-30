"""
LeetCode 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Approach: One Pass (Iterative / Greedy)
Time Complexity: O(n) 
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: If the list is empty or has one price, no profit can be made
        if not prices:
            return 0
            
        min_price = prices[0]
        profit = 0 

        for i in range(1, len(prices)):
            # Calculate potential profit by selling today
            cost = prices[i] - min_price
            
            # Update global maximum profit
            profit = max(profit, cost)
            
            # Update the minimum purchase price found so far
            min_price = min(min_price, prices[i])

        return profit

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
        
