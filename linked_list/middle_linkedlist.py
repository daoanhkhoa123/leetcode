def middle_linked_list(self, head):
	slow = self.head
	fast = self.head

	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next

	return slow