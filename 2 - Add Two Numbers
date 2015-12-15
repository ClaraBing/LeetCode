# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
     def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tail = ListNode(0) # a dummy node: in case the input is [] []
        curr = tail
        digit = 0
        while l1 != None or l2 != None or digit != 0:
        	if l1 != None:
        		digit += l1.val
        		l1 = l1.next
        	if l2 != None:
        		digit += l2.val
        		l2 = l2.next
        	curr.next = ListNode(digit % 10)
        	digit //= 10
        	curr = curr.next
        return tail.next
