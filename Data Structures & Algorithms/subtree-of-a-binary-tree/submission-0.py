# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #O(m * n) TC and O(m )
        #if subRootTree is empty
        if not subRoot:
            return True
        #if main tree is empty
        if not root:
            return False
        #if both trees are same
        if self.isSameTree(root, subRoot):
            return True
        #recursive call - on left and right subtrees of main tree
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


        #helper function
    def isSameTree(self, s, t):
        #if both trees are empty
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            #recursive function for left and right subtrees
            return (self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right))

        return False
