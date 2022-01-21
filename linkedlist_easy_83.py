class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):

        dummy_head = current = ListNode(None)
        next_node = head

        while next_node:
            if (current.val == next_node.val):
                current.next = None
            else:
                current.next = next_node
                current = next_node
            next_node = next_node.next

        return dummy_head.next
