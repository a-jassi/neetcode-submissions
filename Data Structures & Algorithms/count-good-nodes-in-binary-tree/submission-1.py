# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, greatest):
            if not node:
                return 0
            
            isGood = 1 if node.val >= greatest else 0
            newGreatest = max(greatest, node.val)
            
            return isGood + dfs(node.left, newGreatest) + dfs(node.right, newGreatest)
        
        return dfs(root, float("-infinity"))
