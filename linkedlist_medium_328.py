#328


def oddEvenList(head):

    if head == None:
        return None

    odd = head
    even_head = even = ListNode(None)
    current = head.next

    count = 0

    while current:
        if count % 2 == 0:
            even.next = current
            even = even.next
        else:
            odd.next = current
            odd = odd.next
        count += 1
        current = current.next

    even.next = None
    odd.next = even_head.next

    return head
