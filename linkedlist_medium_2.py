class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    total = 0

    current_1 = l1
    count_1 = 0
    current_2 = l2
    count_2 = 0

    while current_1:
        total += current_1.val * 10 ** count_1
        count_1 += 1
        current_1 = current_1.next

    while current_2:
        total += current_2.val * 10 ** count_2
        count_2 += 1
        current_2 = current_2.next

    
    dummy_head = prev_node = ListNode(0)
    
    if total == 0:
        return prev_node

    while total > 0:
        digit = total % 10
        current_node = ListNode(digit)
        prev_node.next = current_node
        prev_node = current_node
        total = total // 10

    return dummy_head.next