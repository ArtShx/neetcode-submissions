# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        queue = [(root, 0)]
        while queue:
            node, height = queue.pop(0)
            depth = max(depth, height)

            if node is None:
                continue
            queue.append((node.left, height+1))
            queue.append((node.right, height+1))

        return depth
