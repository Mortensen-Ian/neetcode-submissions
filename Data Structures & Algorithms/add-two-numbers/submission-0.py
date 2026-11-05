# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry1 = 0
        curl1, curl2 = l1, l2
        prev = None
        while curl1 and curl2:
            total = curl1.val + curl2.val + carry1
            carry1 = total // 10
            curl1.val = total % 10
            prev = curl1
            curl1 = curl1.next
            curl2 = curl2.next
        cur = curl1
        if curl2:
            cur = curl2
            prev.next = cur
        while cur:
            total = cur.val + carry1
            carry1 = total // 10
            cur.val = total % 10
            prev = cur
            cur = cur.next
        if carry1 > 0:
            prev.next = ListNode(carry1, None)
        return l1


        