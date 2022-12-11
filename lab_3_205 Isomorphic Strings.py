'''
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if not s and not t:
            return True
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if not dict_s.get(s[i]):
                dict_s[s[i]] = t[i]
            else:
                if t[i] != dict_s.get(s[i]):
                    return False
                
            if not dict_t.get(t[i]):
                dict_t[t[i]] = s[i]
            else:
                if s[i] != dict_t.get(t[i]):
                    return False
        return True