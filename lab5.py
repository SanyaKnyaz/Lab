'''
2181. Merge Nodes in Between Zeros
https://leetcode.com/problems/merge-nodes-in-between-zeros/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        L = []
        while head:
            L.append(head.val)
            head = head.next
        cur = ListNode(-1)
        res = cur
        summ = 0
        for c in L:
            if c == 0:
                if summ!=0:
                    cur.next = ListNode(summ)
                    cur = cur.next
                    summ = 0
            summ += c
        return res.next