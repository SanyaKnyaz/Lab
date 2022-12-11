'''
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summa = {}
        summa[0] = 1
        counter = 0
        current_summa = 0
        for item in nums:
            current_summa += item
            counter += summa.get(current_summa - k, 0)
            summa[current_summa] = summa.get(current_summa, 0) + 1
        return counter