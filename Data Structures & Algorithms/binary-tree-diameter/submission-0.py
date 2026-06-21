# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #post order traversal - left -> right -> node O(n) TC and O(n) SC

        res = 0

        #return height
        def dfs(root):

            if not root:
                return 0

            nonlocal res

            left = dfs(root.left)
            right = dfs(root.right)
            #calculate diameter
            res = max(res, left + right)

            #return height    
            return 1 + max(left, right)

        dfs(root)
        return res




        