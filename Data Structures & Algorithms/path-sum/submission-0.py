# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def dfs(node: Optional[TreeNode], current: int):
            
            if node is None:
                return False
            current += node.val
            if dfs(node.left, current):
                return True
            if dfs(node.right, current):
                return True
            
            is_leaf = node.left is None and node.right is None
            return current == targetSum and is_leaf

        return dfs(root, 0)