# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def postTrav(root):
            if root is None:
                return
            postTrav(root.left)
            postTrav(root.right)
            result.append(root.val)
        postTrav(root)
        return result
