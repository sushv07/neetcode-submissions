# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def preorder(node, arr):

            if not node:

                arr.append("N")

                return

            arr.append(str(node.val))

            preorder(node.left, arr)

            preorder(node.right, arr)

        rootArr = []

        subArr = []

        preorder(root, rootArr)

        preorder(subRoot, subArr)

        return ",".join(subArr) in ",".join(rootArr)