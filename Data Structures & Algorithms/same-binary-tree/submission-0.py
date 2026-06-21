# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #O(n) TC and O(n) SC
        #base cases
        #empty trees
        if not p and not q:
            return True
        #either is a non-empty tree
        if not p or not q or p.val != q.val:
            return False
        #dfs recursion
        return ((self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)))
        