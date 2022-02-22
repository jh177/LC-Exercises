class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head
        
        dummy = ListNode()
        dummy.next = head
        prev_node = dummy
        current = head
        
        while current and current.next:
            first_node = current
            second_node = current.next
            
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            prev_node = first_node
            current = first_node.next
        
        return dummy.next