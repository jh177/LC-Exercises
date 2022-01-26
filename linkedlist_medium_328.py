#328


def oddEvenList(head):

    odd = ListNode(None)
    even_head = ListNode(None)
    even = ListNode(None)
    even_head.next = even

    current = head

    count = 1

    while current is not None:
    		if count % 2 == 1:
       		odd.next = current
            odd = current
        else:
        	even.next = current
            even = current
        
        current = current.next
        count += 1
    
    
    odd.next = even_head.next
    
    return head