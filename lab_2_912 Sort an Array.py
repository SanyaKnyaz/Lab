'''
912. Sort an Array
https://leetcode.com/problems/sort-an-array/
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        l = len(nums)
        a = self.sortArray(nums[:l//2])
        b = self.sortArray(nums[l//2:])
        i, j, x = 0, 0, 0
        # сортировка слиянием
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                nums[x] = a[i]
                i = i+1
            else:
                nums[x] = b[j]
                j = j+1
            x = x+1
        while i < len(a):
            nums[x] = a[i]
            x = x+1
            i = i+1
        while j < len(b):
            nums[x] = b[j]
            x = x+1
            j = j+1
        return nums