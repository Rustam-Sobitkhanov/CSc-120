"""
File: linked_list_short.py
Author: Rustambek Sobithanov
Purpose: The following functions perform various tasks stated in the specs of
         Short Project 4
"""
from list_node import *


def list_to_array(head):
    """
    converts a linked list to an array containing the same values
    :param head: reference to the first element of a linked list
    :return: an array, with the same values, in the same order
    """
    cur = head
    the_list = []
    while cur is not None:
        the_list.append(cur.val)
        cur = cur.next
    return the_list


def array_to_list(data):
    """
    converts an array to a linked list
    :param data: an array of values (perhaps zero length)
    :return: a linked list, containing the same nodes, in the same order
    """
    if len(data) == 0:
        head = None
    else:
        head = ListNode(data[0])
        cur = head
        for i in range(1, len(data)):
            cur.next = ListNode(data[i])
            cur = cur.next
    return head


def list_length(head):
    """
    finds the length of a linked list and returns it
    :param head: reference to the first element of a linked list
    :return: the length of a linked list
    """
    cur = head
    length = 0
    while cur is not None:
        length += 1
        cur = cur.next
    return length


def split_list(old_head):
    """
    takes a linked list, and splits it into two at the middle
    :param old_head: reference to the first element of a linked list
    :return: a tuple, with the heads of the two lists
    """
    cur = old_head
    length = 0
    if old_head is None:
        head_1 = None
        head_2 = None
        return (head_1, head_2)
    else:
        while cur is not None:
            length += 1
            cur = cur.next

        if length % 2 == 0:
            middle = int(length / 2) - 1
            cur = old_head
            for i in range(middle):     # moves along the linked list until
                cur = cur.next          # it finds the obj in the middle
            head2 = cur.next
            cur.next = None
            head1 = old_head
            return (head1, head2)

        middle = int(length / 2)
        cur = old_head
        for i in range(middle):
            cur = cur.next
        head2 = cur.next
        cur.next = None
        head1 = old_head
        return (head1, head2)
