'''
278. First Bad Version
https://leetcode.com/problems/first-bad-version/description/
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
          mid = (left + right) // 2
          if isBadVersion(mid):
            right = mid
          else:
            left = mid + 1

        return left