# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        while l1:
            n1.append(str(l1.val))
            l1 = l1.next
        n1 = int("".join(n1[::-1])) if n1 else 0

        n2 = []
        while l2:
            n2.append(str(l2.val))
            l2 = l2.next
        n2 = int("".join(n2[::-1])) if n2 else 0

        
        total = n1+n2

        l3 = None
        for digit in str(total):
            if l3 is None:
                l3 = ListNode(int(digit))
            else:
                node = ListNode(int(digit))
                node.next = l3
                l3 = node
            
            nextval = l3.next.val if l3.next else None
        return l3