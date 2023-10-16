# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0

            maxL = dfs(root.left)
            maxR = dfs(root.right)
            maxL = max(0, maxL)
            maxR = max(0, maxR)

            res[0] = max(res[0], root.val + maxL + maxR)

            return root.val + max(maxL , maxR)
        
        dfs(root)
        return res[0]
        



        
