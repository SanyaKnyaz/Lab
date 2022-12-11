'''
1. Two Sum
https://leetcode.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums:
                if nums.index(res) == i:
                    continue
                return i, nums.index(res)