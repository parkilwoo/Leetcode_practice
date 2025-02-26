# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        deque_ = deque()

        if root:
            deque_.append(root)
        
        level = 0
        while deque_:
            cur_deque_len = len(deque_)
            for i in range(cur_deque_len):
                cur_node = deque_.popleft()
                left = cur_node.left
                if left:
                    deque_.append(left)
                right = cur_node.right
                if right:
                    deque_.append(right)
            level += 1

        return level
        