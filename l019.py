# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self.next == None:
			return str(self.val)
		return str(self.val) + " " + self.next.__repr__()

# two pointers
def t(head, n):
	if head == None:
		return head
	slow, fast = head, head
	for i in range(n):
		fast = fast.next
	if fast == None:
		return head.next
	while fast.next != None:
		fast = fast.next
		slow = slow.next
	slow.next = slow.next.next
	return head

# use a dictionary to keep track of nodes -- slow
def f(head, n):
	curr = head
	t = {}
	cnt = 1
	while curr != None:
		t[cnt] = curr
		cnt += 1
		curr = curr.next
	if cnt-n-1 == 0:
		return head.next
	t[cnt-n-1].next = t[cnt-n].next
	return head

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

l = n1