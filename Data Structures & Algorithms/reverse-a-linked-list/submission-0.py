# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = None
        while head:
            next = ListNode(head.val, next=out)
            out = next
            head = head.next
        return out
        