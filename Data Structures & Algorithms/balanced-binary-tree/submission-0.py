# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #TC O(n) - each node is traversed exactly once
        #SC O(h) - function calls for each sub trees are stored in the recursion stack. h - height of the tree
        def dfs(root):
            #if null, no node
            if not root:
                return [True, 0]

            #post-order traversal - left, right, current node
            left, right = (dfs(root.left), dfs(root.right))
            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

        