# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #DFS - O(n) TC and O(h) SC
        if not root:
            return None

        #swap children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        #apply recursion
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        