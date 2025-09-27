'''
160. Intersection of two linked lists

Given the heads of two singly linked-lists headA and headB, return the node at which
the two lists intersect. If the two lists have no intersection at all, return null.
'''

from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         currentA = headA
#
#         while currentA:
#             currentB = headB
#
#             while currentB:
#                 if currentA == currentB:
#                     return currentA 
#                 currentB = currentB.next 
#
#             currentA = currentA.next
#
#         return None
#


class Solution:
    def getIntersectionNode(self, headA : ListNode, headB : ListNode) -> Optional[ListNode]:
        currentA = headA
        currentB = headB

        while currentA != currentB:
            currentA = currentA.next if currentA else headB
            currentB = currentB.next if currentB else headA

        return currentA
