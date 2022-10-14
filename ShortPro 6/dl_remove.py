"""
File: dl_remove.py
Author: Rustambek Sobithanov
Purpose: The following function removes a specified node from a given
         doubly-linked list.
"""
from dlist_node import *


def dl_remove(head, a_node):
    # deals with the case when we have to remove the head
    if head.val == a_node.val:
        if head.next is not None:   # deals with the situation when there is
            head.next.prev = None   # only one node in the list
        else:
            return None
        return head.next
    next_node = a_node.next
    prev_node = a_node.prev
    prev_node.next = next_node
    # deals with the case when we have to remove the last node
    if next_node is not None:
        next_node.prev = prev_node
    return head
