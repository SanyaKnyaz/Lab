'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram
'''
#def my_quick_sort(l):
#    if len(l) < 2:
#        return l
#    mid = len(l) // 2
#    left, middle, right = [], [], []
#    for x in l:
#        if x < l[mid]:
#            left.append(x)
#        elif x > l[mid]:
#            right.append(x)
#        else:
#            middle.append(x)
#    return my_quick_sort(left) + middle + my_quick_sort(right)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)
        return dict_s == dict_t
        
        #s = my_quick_sort(s)
        #t = my_quick_sort(t)
        #return s == t