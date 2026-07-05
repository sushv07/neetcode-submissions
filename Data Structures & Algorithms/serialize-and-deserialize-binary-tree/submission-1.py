# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    #dfs preorder traversal - O(n) TC and O(n) SC
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return       
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)  
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #split the result list using comma delimiter
        vals = data.split(",")
        #pointer to increment the list indices
        self.i = 0

        def dfs():
            #subTree end check
            if vals[self.i] == 'N':
                self.i += 1
                return None
            #construct Tree
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

            



        