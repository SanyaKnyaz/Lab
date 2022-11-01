'''
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = ListNode()
        cur.next = head
        prev = cur
        while (head):
            if head.val == val:
                prev.next = head.next
            else:
                prev = head            
            head = head.next
        return cur.next