'''
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        left = 0
        right = len(nums) - 1
        ind = len(nums) - 1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                res[ind] = nums[right] * nums[right]
                ind -= 1
                right -= 1
            else:
                res[ind] = nums[left] * nums[left]
                ind -= 1
                left += 1
        return res
