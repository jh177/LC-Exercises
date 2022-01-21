from json.encoder import INFINITY
from typing import List


class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


def mergeTwoLists(list1, list2):

    dummyHead = current = ListNode(None)
    node1 = list1
    node2 = list2

    while node1 and node2:
        if (node1.val <= node2.val):
            current.next = node1
            current = node1
            node1 = node1.next
        else:
            current.next = node2
            current = node2
            node2 = node2.next

    if (node1):
            current.next = node1
    if (node2):
            current.next = node2

    return dummyHead.next
