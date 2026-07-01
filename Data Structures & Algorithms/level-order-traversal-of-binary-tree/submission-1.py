# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #O(n) TC and O(n/2)-> O(n) SC
        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            #bfs to traverse each level of tree    
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res.append(level)
        
        return res


                


        