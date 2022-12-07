'''
268. Missing Number
https://leetcode.com/problems/missing-number/
'''
def my_quick_sort(l):
    if len(l) < 2:
        return l
    mid = len(l) // 2
    left, middle, right = [], [], []
    for x in l:
        if x < l[mid]:
            left.append(x)
        elif x > l[mid]:
            right.append(x)
        else:
            middle.append(x)
    return my_quick_sort(left) + middle + my_quick_sort(right)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = my_quick_sort(nums)
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] != mid:
                right = mid
            else:
                left = mid + 1
        return left
