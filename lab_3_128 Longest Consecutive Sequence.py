'''
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        dict_nums = {}
        arr_nums = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] not in dict_nums:
                dict_nums[nums[i]] = i
        for j in nums:
            current = j
            counter = 1
            if arr_nums[dict_nums[j]]:
                continue
            while current + 1 in dict_nums:
                current += 1
                index = dict_nums[current]
                if arr_nums[index]:
                    counter += arr_nums[index]
                    break
                else:
                    arr_nums[index] = 1
                    counter += 1
            arr_nums[dict_nums[j]] = counter
            result = max(result, counter)
        return result
