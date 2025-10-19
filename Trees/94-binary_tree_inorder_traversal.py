'''
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its values

'''

from typing import Optional, List

# Definition for a binary tree node 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
        

class Solution: 
    def inorderTraversal(self, root : Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left)  + [root.val] + self.inorderTraversal(root.right)
    

if __name__ == '__main__':
    solution = Solution() 
    #####