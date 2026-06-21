# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #Iterative DFS Optimal - O(n) TC and O(n) space complexity 
        n = 0
        stack = []
        curr = root

        while curr or stack:
            #iterate through left sub trees
            while curr:
                stack.append(curr)            
                curr = curr.left
            
            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val
            #if val not found yet, iterate through right subtrees
            curr = curr.right        