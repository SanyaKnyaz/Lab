'''
268. Missing Number
https://leetcode.com/problems/missing-number/
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summa = 0
        for i in nums:
            summa += i
        res = int((1+len(nums)) * len(nums) / 2 - summa)
        return res 
