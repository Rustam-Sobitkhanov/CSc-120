"""
File: linked_list_recursion.py
Author: Rustambek Sobithanov
Purpose: The following functions showcase the algorithms which are required in
         the specs of ShortPro 8
"""


def is_sorted(head):
    if head is None:
        return True
    cur = head
    while cur.next is not None:
        if cur.val > cur.next.val:
            return False
        else:
            cur = cur.next
    return True


def is_sorted_recursive(head):
    if head is None:
        return True
    if head.next is None:
        return True
    if head.val > head.next.val:
        return False
    return is_sorted_recursive(head.next)
