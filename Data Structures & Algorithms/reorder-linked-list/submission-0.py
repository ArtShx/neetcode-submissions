# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        r = -1
        while head:
            arr.append(head)
            head = head.next
            r += 1

        l = 0

        while l < r:
            arr[l].next = arr[r]
            if l+1 <= r:
                arr[r].next = arr[l+1]
            l+=1
            r-=1
        arr[l].next = None


        """
        2 4 6 8
        l = 0, r = 3
            2 8  
        l = 1, r = 2
            2 8 4 6

        """

