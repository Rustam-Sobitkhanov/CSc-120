"""
File: .py
Author: Rustambek Sobithanov
Purpose: The following functions perform the operations explained in the
         specs of Long Project 5.
"""
from list_node import *


def is_sorted(head):
    """
    determines if the given list is sorted or not
    :param head: reference to the first node of a linked list
    :return: a boolean value
    """
    if head is None:
        return True
    else:
        cur = head
        while cur.next is not None:
            if cur.val > cur.next.val:
                return False
            cur = cur.next
        return True


def list_sum(head):
    """
    iterates through a list and adds all the values together
    :param head: reference to the first node of a linked list
    :return: integer, indicating the sum of all the values inside a list
    """
    if head is None:
        return 0
    else:
        cur = head
        overall = 0
        while cur is not None:
            overall += cur.val
            cur = cur.next
        return overall


def partition_list(head):
    """
    creates two lists, the values of which are alternate to each other
    :param head: reference to the first node of a linked list
    :return: two lists
    """
    cur = head
    counter = 1
    odd_list = cur
    if cur.next is not None:
        even_list = odd_list.next
    else:
        return odd_list, None
    cur = even_list.next
    list1 = odd_list
    list2 = even_list
    while cur is not None:
        if counter % 2 == 1:
            list1.next = cur
            list1 = cur
            cur = cur.next
            counter += 1
        else:
            list2.next = cur
            list2 = cur
            cur = cur.next
            counter += 1
    list1.next = None
    list2.next = None
    return odd_list, even_list


def accordion_4(head, start_pos):
    """
    builds a list from the given list - the values of the new list are
    each fourth value of the given list
    :param head: reference to the first node of a linked list
    :param start_pos: an integer indicating the position of the first
                      node of the list that is returned later
    :return: a list
    """
    if head is None:
        return None
    else:
        counter = 0
        cur = head
        while counter != start_pos:
            counter += 1
            cur = cur.next
        return_list = cur
        list1 = cur
        while cur is not None and cur.next is not None:
            i = 0
            while i < 3 and cur.next is not None:
                cur = cur.next
                i += 1
            else:
                list1.next = cur.next
                list1 = cur.next
                cur = cur.next
        return return_list


def pair(list1, list2):
    """
    builds new ListNode objects, where the value of each one is a tuple,
    consisting of one value from the first list, and one value from
    the second list, in the same order as they existed in those input lists
    :param list1: reference to a head of a linked list
    :param list2: reference to a head of a linked list
    :return: a list the values of which are tuples
    """
    if list1 is None or list2 is None:
        return None
    else:
        head = ListNode((list1.val, list2.val))
        head_track = head
        cur1 = list1.next
        cur2 = list2.next
        while cur1 is not None and cur2 is not None:
            head_track.next = ListNode((cur1.val, cur2.val))
            head_track = head_track.next
            cur1 = cur1.next
            cur2 = cur2.next
        return head

