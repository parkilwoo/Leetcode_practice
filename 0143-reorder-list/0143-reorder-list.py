# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. 리스트의 반절 찾기(두배 빠른 포인터 이용)
        normal = double = head
        while double and double.next:
            normal = normal.next
            double = double.next.next

        # 2. 반절 뒤의 리스트들을 뒤집기
        prev, curr = None, normal
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp            
        
        # 3. Merge
        first, second = head, prev
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2        
