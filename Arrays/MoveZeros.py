"""
LeetCode 283: Move Zeroes
Difficulty: Easy
Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
""" 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        j = -1
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        
        if j == -1:
            return

        for i in range(j+1,n):
            if nums[i]!=0:
                swap(i,j)
                j+=1
            

        
