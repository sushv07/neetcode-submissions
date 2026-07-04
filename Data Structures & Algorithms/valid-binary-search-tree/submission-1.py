# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #TC - O(n) and O(n) SC
        #recursive function to check if it is a valid bst
        def valid(node, left, right):
            #empty BST check
            if not node:
                return True
            #BST property check if node.val strictly between left and right
            if not (left < node.val and right > node.val):
                return False
            #recursive calls - left and right subtrees
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        #call root
        return valid(root, float("-inf"), float("inf"))

            

        