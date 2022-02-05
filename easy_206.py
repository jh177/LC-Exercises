class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        new_head = None
        
        while current:
            next = current.next
            if next == None:
                new_head = current
            current.next = prev
            prev = current
            current = next
        
        return new_head