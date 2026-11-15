# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        dummy = head
        while dummy:
            size += 1
            dummy = dummy.next

        if size == 1 or size == 0:
            return None
        n = abs(n - size) if n >= size else size - n

        itr = 0
        node = head
        prev = None
        if n == 0:
            return head.next

        while node:
            if itr == n-1:
                prev = node
            if itr == n:
                prev.next = node.next
            node = node.next
            itr += 1
        return head
            





