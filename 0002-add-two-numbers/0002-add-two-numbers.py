# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum_list = []
        is_ten_upper = False
        while l1 or l2:
            l1_v = l1.val if l1 is not None else 0
            l2_v = l2.val if l2 is not None else 0
            sum_v = l1_v + l2_v
            if is_ten_upper == True:
                sum_v += 1
            if sum_v > 9:
                is_ten_upper = True
                sum_v -= 10
            else:
                is_ten_upper = False
            sum_list.append(sum_v)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if is_ten_upper:
            sum_list.append(1)
        
        before_node = None
        for v in sum_list[::-1]:
            node = ListNode(v)
            if before_node:
                node.next = before_node
            before_node = node

        return before_node

