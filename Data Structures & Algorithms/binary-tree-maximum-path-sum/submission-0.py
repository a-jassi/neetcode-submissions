# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(curr):
            if not curr:
                return 0
            
            leftMax = max(dfs(curr.left), 0)
            rightMax = max(dfs(curr.right), 0)

            maxWithSplit = curr.val + leftMax + rightMax
            res[0] = max(res[0], maxWithSplit)

            return curr.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]


