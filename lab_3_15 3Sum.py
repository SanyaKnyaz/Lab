'''
15. 3Sum
https://leetcode.com/problems/3sum/
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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = my_quick_sort(nums)
        triples = list()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    triples.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return triples