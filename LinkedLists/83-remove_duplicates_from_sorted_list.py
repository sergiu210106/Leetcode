'''
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return
the linked list sorted as well.
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        last = dummy

        current = head
        while current:
            if not current.next or current.val != current.next.val:
                new_node = ListNode(val = current.val, next = None)
                last.next = new_node
                last = last.next
            current = current.next

        return dummy.next
