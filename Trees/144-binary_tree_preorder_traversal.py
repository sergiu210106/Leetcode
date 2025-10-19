'''
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder 
traversal of its nodes' values.
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 
    
class Solution:
    def preorderTraversal (self, root : Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
if __name__ == "__main__":
    solution = Solution()