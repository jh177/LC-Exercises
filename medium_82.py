# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# prev node for previous node -- dummy at first, moves when slow moves, moves to slow prev
# current node for current node -- moves to fast if slow val == fast val
# fast node for next nodes -- moves to next if fast val == slow val


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = prev = ListNode()
        prev.next = head
        current = head
        
        while current:
            fast = current.next
            duplicated = False
            while fast and current.val == fast.val:
                fast = fast.next
                duplicated = True
            
            if not duplicated:
                prev = current
                
            prev.next = fast
            current = fast
        
        return dummy.next