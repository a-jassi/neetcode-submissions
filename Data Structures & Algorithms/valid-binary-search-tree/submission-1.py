# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lowerBound, upperBound):
            if not node:
                return True
            
            if lowerBound >= node.val or node.val >= upperBound:
                return False

            newLowerBound = max(lowerBound, node.val)
            newUpperBound = min(upperBound, node.val)
        
            return dfs(node.left, lowerBound, newUpperBound) and dfs(node.right, newLowerBound, upperBound)
        
        return dfs(root, float("-inf"), float("inf"))