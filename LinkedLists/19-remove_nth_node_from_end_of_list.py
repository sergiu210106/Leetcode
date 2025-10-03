'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the Nth node from the end of the list and return its head.
'''

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head : Optional[ListNode], n : int) -> Optional[ListNode]:
       size = 0
       current = head
       while current:
           current = current.next
           size += 1

        

if __name__ == '__main__':
    solution = Solution()
