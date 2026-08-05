# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd = 0
        def dfs(node):
            nonlocal maxd
            if node is None:
                return 0
            hleft = dfs(node.left)
            hright = dfs(node.right)
            maxd = max(maxd, hleft + hright)
            return 1 + max(hleft, hright)

        dfs(root)
        return maxd
