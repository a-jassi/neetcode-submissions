# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(curr):
            if not curr:
                return [0, 0]
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            diameter = max(left[0], right[0], left[1] + right[1])

            return (diameter, 1 + max(left[1], right[1]))
        
        return dfs(root)[0]