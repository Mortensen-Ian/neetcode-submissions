# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import bisect
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current = []
        for head in lists:
            if head:
                current.append(head)
        current.sort(key=lambda nd: nd.val)

        start = ListNode()
        cur = start
        while current:
            cur.next = current.pop(0)
            cur = cur.next
            ## Insert new next node into current into current.
            if cur.next:
                bisect.insort(current, cur.next, key=lambda x: x.val)
        return start.next