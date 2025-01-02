# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def traverseWithOrder(level: int, root: Optional[TreeNode]):
            if (root is None):
                return
            
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)

            traverseWithOrder(level + 1, root.left)
            traverseWithOrder(level + 1, root.right)

        traverseWithOrder(0, root)

        return res
