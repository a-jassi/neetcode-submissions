# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(node, subNode):
            if not node and not subNode:
                return True
            if not node or not subNode:
                return False
            
            left = isEqual(node.left, subNode.left)
            right = isEqual(node.right, subNode.right)
            return left and right and node.val == subNode.val
        
        if not subRoot:
            return True
        if not root:
            return False

        if isEqual(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
