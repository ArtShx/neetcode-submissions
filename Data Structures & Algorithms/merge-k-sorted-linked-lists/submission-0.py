# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        pointers = [0] * n
        dummy = ListNode()
        head = dummy

        i = 0
        while True:
            #print(i)
            selected_list = -1
            minvalue = float("inf")
            for l in range(n):
                if lists[l] and lists[l].val < minvalue:
                    minvalue = lists[l].val
                    selected_list = l
            
            if selected_list == -1:
                break
            #print("\t", lists[selected_list].val)
            head.next = lists[selected_list]
            head = head.next

            lists[selected_list] = lists[selected_list].next
            i+=1

        return dummy.next