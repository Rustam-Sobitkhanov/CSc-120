"""
File: linked_list_recursion_part2.py
Author: Rustambek Sobithanov
Purpose: The following functions meet the requirements of LongPro 8
"""
from list_node import *


def array_to_list_recursive(data):
    """
    turns the given array into a linked list
    :param data: an array
    :return: first node of the linked list
    """
    if not data:
        return None
    if data == [data[-1]]:      # handles the case when there is only one element in the list
        head = ListNode(data[-1])
        return head
    head = ListNode(data[0])
    head.next = array_to_list_recursive(data[1:])
    return head


def accordion_recursive(head):
    """
    returns a linked list whose nodes are every other node of a previous linked list
    :param head: first node of a linked list
    :return: first node of the made linked list
    """
    if head is None:
        return None
    if head.next is None:
        return None
    if head.next.next is None:
        return head.next
    cur = head.next
    cur.next = accordion_recursive(head.next.next)
    return cur


def pair_recursive(head1, head2):
    """
    given 2 linked lists, returns a linked list whose
    nodes are a tuple pair of nodes of given lists
    :param head1: a linked list
    :param head2: a linked list
    :return: a linked list whose nodes are a tuple pair of nodes of given lists
    """
    if head1 is None or head2 is None:
        return None
    if head1.next is None or head2.next is None:
        value = (head1.val, head2.val)
        head = ListNode(value)
        return head
    value = (head1.val, head2.val)
    head = ListNode(value)
    head.next = pair_recursive(head1.next, head2.next)
    return head

