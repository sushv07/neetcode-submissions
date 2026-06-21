# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #TC O(n^2) TC and O(n^2) SC
        #base case for all subtrees
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        #find its index in inorder array to split into left and right subtrees
        mid = inorder.index(preorder[0])
        #recurse left
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        #recurse right
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


        