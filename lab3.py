'''
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def init(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lst = set()
        cur = headA
        while cur:
            lst.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in lst:
                return cur
            cur = cur.next
        return None