# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(left, right):
            if left is None and right is None:
                return True
            if (left is None and right) or (left and right is None):
                return False
            if left.val != right.val:
                return False
            return is_same_tree(left.left, right.left) and is_same_tree(left.right, right.right)

        #print(root, subRoot.val, root.val if root else -1)
        if is_same_tree(root, subRoot):
            return True
        if root is None and subRoot:
            return False

        leftsame = self.isSubtree(root.left, subRoot)
        rightsame = self.isSubtree(root.right, subRoot)
        if leftsame or rightsame:
            return True
        return False
        
        
