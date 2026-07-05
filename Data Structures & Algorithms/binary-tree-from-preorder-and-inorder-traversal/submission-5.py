# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #O(n) TC and O(n) SC
        #build hashmap for inorder array - val : idx
        indices = {val: idx for idx, val in enumerate(inorder)}

        #index for preorder array
        self.pre_idx = 0

        #recursive function for left and right subtrees
        def dfs(l, r):
        #base case : when to end a subtree - invalid left and right boundaries - no elements between them
            if l > r:
                return None

            #get the root value from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            #Build root
            root = TreeNode(root_val)
            #find the mid to make split - left and right subtrees
            mid = indices[root_val]
            #recursive calls - to build left and right sub trees
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(preorder) - 1)


        


        