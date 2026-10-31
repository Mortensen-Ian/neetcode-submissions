# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #start from the middle
        cur = head
        cur2 = head.next
        while cur2 and cur2.next:
            cur = cur.next
            cur2 = cur2.next.next
        temp = cur
        cur = cur.next
        temp.next = None
        end = self.Reverse(cur)
        cur = head
        while end:
            left = cur.next
            right = end.next
            cur.next = end
            end.next = left
            cur = left
            end = right        
        
    def Reverse(self, head):
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
            