# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def traverse(node, current):
            #print(node, current)
            if node is None or current == k:
                return  node, current
            ##print(node.val, current)
            if node.left:
                left, current = traverse(node.left, current)
            
                if current == k:
                    return  left, current

            current += 1
            #print("\t", node.val, current)
            if current == k:
                return  node, current

            if node.right:
                right, current = traverse(node.right, current)

                if current == k:
                    return  right, current
            return node, current
        foundnode, kitem = traverse(root, 0)
        return foundnode.val