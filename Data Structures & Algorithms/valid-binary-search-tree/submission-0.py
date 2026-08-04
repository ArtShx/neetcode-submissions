# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = float("inf")
        def traverse(node, minv, maxv):
            if node is None:
                return True
            #print(minv, node.val, maxv)
            if not (minv < node.val < maxv):
                return False
            if not traverse(node.left, min(minv, node.val), min(maxv, node.val)):
                return False
            if not traverse(node.right, max(minv, node.val), max(maxv, node.val)):
                return False
            return True
        
        return traverse(root, -inf, inf)