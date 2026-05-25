# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(curr, currSub):
            if not curr and not currSub:
                return True
            if not curr or not currSub:
                return False
            
            if curr.val != currSub.val:
                return False
            
            return isEqual(curr.left, currSub.left) and isEqual(curr.right, currSub.right)
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            return isEqual(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)