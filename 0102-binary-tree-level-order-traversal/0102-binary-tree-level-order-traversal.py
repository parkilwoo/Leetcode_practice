from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        que = deque()
        que.append(root)
        while que:
            que_size = len(que)
            level_array = []
            for _ in range(que_size):
                n = que.popleft()
                level_array.append(n.val)
                if n.left:
                    que.append(n.left)
                if n.right:
                    que.append(n.right)

            res.append(level_array)

        return res
            
        