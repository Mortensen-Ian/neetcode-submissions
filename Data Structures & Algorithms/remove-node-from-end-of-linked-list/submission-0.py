# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        cur = head
        while cur:
            total += 1
            cur = cur.next
        
        count = 0
        cur = head
        prev = None
        while total - count != n:
            count += 1
            prev = cur
            cur = cur.next
        if prev:
            prev.next = cur.next
            return head
        else:
            return cur.next
        
        