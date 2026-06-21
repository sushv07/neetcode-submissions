# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #TC O(n) TC and O(n) SC
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(len(q)):
                node = q.popleft()
                #handles null values
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            #handles null values  - incase last node is null    
            if rightSide:
                res.append(rightSide.val)
            
        return res



        