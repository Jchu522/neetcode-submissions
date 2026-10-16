# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = ListNode(0, head)
        slow = ListNode (0, fast)
        while fast != slow:
            if fast.next == None or fast.next.next == None:
                return False
            fast.next = fast.next.next
            slow = head
            head = head.next
            fast = fast.next
            
        return True