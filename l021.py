# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self.next == None:
			return str(self.val)
		return str(self.val) + " " + self.next.__repr__()

def f(l1, l2):
	c1, c2 = l1, l2
	ret = ListNode(0)
	head = ret
	while c1 != None and c2 != None:
		if c1.val > c2.val:
			ret.next = c2
			ret = ret.next
			c2 = c2.next
		else:
			ret.next = c1
			ret = ret.next
			c1 = c1.next
	ret.next = c2 if c1 == None else c1
	return head.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n1.next = n2
n2.next = n5

n3.next = n4
n4.next = n6