# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Do a nextNode pointer
        #Have a cur pointer
        #Have a counter to check if k is hit.
        prev = None
        cur = head
        while cur:
            last = cur
            first = prev
            short = False
            for i in range(k):
                if cur:
                    first = cur
                    cur = cur.next
                else:
                    short = True
                    break
            if short:
                if prev:
                    prev.next = last
                break
            first.next = None
            if prev:
                prev.next = self.reverse(last)
            else:
                head = self.reverse(last)
            prev = last
        return head

    def reverse(self, head):
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
