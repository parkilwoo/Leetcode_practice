# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs로 최대 깊이 찾기
        
        if not root:
            return 0

        max_depth = 0
        def dfs(node, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)

        dfs(root, 1)

        return max_depth