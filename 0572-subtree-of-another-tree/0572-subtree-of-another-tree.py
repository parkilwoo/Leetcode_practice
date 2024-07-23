# Definition for a binary tree node.
#  class TreeNode:
#      def __init__(self, val=0, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
#      def is_same(self, check_tree: TreeNode):
        
        
#         return true
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.is_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def is_same(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val != subRoot.val: return False
        return self.is_same(root.left, subRoot.left) and self.is_same(root.right, subRoot.right)