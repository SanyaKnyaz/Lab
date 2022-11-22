'''
441. Arranging Coins
https://leetcode.com/problems/arranging-coins/description/
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid * (mid + 1) // 2 <= n:
                left = mid
            else:
                right = mid
        if right * (right + 1) // 2 <= n:
            return right
        return left