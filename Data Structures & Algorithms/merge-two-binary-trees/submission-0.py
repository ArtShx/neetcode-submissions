# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def make(left, right):
            if left is None and right is None:
                return
            if left is None:
                return TreeNode(right.val)
            if right is None:
                return TreeNode(left.val)
            return TreeNode(left.val + right.val)
        
        def dfs(left, right):
            node = make(left, right)
            if node is None:
                return
            node.left = dfs(left.left if left else None, right.left if right else None)
            node.right = dfs(left.right if left else None, right.right if right else None)
            return node
        
        new = dfs(root1, root2)
        return new
