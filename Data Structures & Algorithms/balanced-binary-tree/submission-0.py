# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs(node, height):
            if node is None:
                return True, height
            height += 1
            l, hl = dfs(node.left, height)
            r, hr = dfs(node.right, height)
            if l is False or r is False:
                return False, -1
            balanced = abs(hl-hr) <= 1
            if not balanced:
                return False, -1
            return balanced, max(hl, hr)

        return dfs(root, 0)[0]