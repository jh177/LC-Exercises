class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = slow = head
        while (n > 0):
            fast = fast.next
            n = n-1

        if (fast == None):
            return head.next

        while fast != None and fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
