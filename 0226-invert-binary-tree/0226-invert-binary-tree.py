# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive(root: Optional[TreeNode]):
            if not root:
                return None
            
            left_tmp = root.left
            right_tmp = root.right
            root.left = right_tmp
            root.right = left_tmp

            recursive(root=root.left)        
            recursive(root=root.right)
        
        recursive(root=root)

        return root