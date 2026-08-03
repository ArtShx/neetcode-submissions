# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        root = head
        while head:
            arr.append(head)
            head = head.next
        sz = len(arr)

        to_remove = sz-n
        if to_remove == 0:
            return root.next
        if n == 1:
            if sz == 1:
                return None
            arr[-2].next = None
            return root
        arr[to_remove-1].next = arr[to_remove+1]
        return root
