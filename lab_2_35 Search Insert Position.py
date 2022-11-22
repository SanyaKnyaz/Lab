'''
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            else:
                if target > nums[i-1] and target < nums[i]:
                    return i
                else:
                    if target > nums[len(nums)-1]:
                        return len(nums)
                    else:
                        if target < nums[0]:
                            return 0