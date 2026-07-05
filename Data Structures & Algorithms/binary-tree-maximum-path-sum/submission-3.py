# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #o(n) TC and O(h) SC
        #global var - to return max path sum
        res = root.val

        #recursive function - to return max path sum without split
        def dfs(root):
            nonlocal res
            #if node empty, no path exists
            if not root:
                return 0

            #compute max path sum for left nodes - recursive calls
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            #ignoring negative node values
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #"Is the path that bends HERE the overall best answer?"
            # → Update global max if yes.
            #compute max path sum with split
            res = max(res, root.val + leftMax + rightMax)
            #return max pth sum without split
            #"What downward sum do I pass up to my parent so it can decide about paths bending at the parent level?" 
            #→ Return for parent to use.
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res





        