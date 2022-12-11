'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dict_strs = {}
        for item in strs:
            tmp = ''.join(my_quick_sort(item))
            if tmp in dict_strs:
                res[dict_strs[tmp]].append(item)
            else:
                ind = len(res)
                res.append([item])
                dict_strs[tmp] = ind
        return res