'''
75. Sort Colors
https://leetcode.com/problems/sort-colors
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(nums==[]):
            return
        s_num = 0
        dl_num = len(nums) - 1
        i = 0
        while i <= dl_num:
            if nums[i] == 2:
                a_2 = nums[i]
                nums[i] = nums[dl_num]
                nums[dl_num] = a_2
                dl_num -= 1
            elif nums[i] == 0:
                a_0 = nums[i]
                nums[i] = nums[s_num]
                nums[s_num] = a_0
                s_num += 1
                i += 1
            else:
                i += 1
            