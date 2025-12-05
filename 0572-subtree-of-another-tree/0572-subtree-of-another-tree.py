# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. Base Case: root가 없으면 비교 자체가 불가능하므로 False
        if not root:
            return False
        
        # 2. 현재 root에서 시작하는 트리가 subRoot와 같은지 확인
        if self.isSameTree(root, subRoot):
            return True
        
        # 3. 아니라면, 왼쪽 자식이나 오른쪽 자식에서 다시 탐색 (재귀)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # 두 트리가 완전히 같은지 확인하는 헬퍼 함수
    def isSameTree(self, p, q):
        # 둘 다 None이면 같음
        if not p and not q:
            return True
        # 둘 중 하나만 None이거나, 값이 다르면 다름
        if not p or not q or p.val != q.val:
            return False
        # 왼쪽과 오른쪽 자식들도 모두 같아야 함
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)