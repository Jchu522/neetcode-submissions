import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        linked = []
        for arr in lists:
            while arr:
                linked.append(arr.val)
                arr = arr.next
        
        linked.sort()
        dummy = ListNode(0, None)
        head = dummy
        for n in linked:
            dummy.next = ListNode(n, None)
            dummy = dummy.next

        return head.next
