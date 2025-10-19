'''
145. Binary Tree Postorder Traversal
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 
    
class Solution:
    def postorderTraversal (self, root : Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
if __name__ == "__main__":
    solution = Solution()