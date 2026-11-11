# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        head = dummy
        carry = 0
        while l1 and l2:
            temp = l1.val + l2.val + carry
            carry = 0
            if temp > 9:
                carry = 1 
                temp -=10
            
            dummy.next = ListNode(temp, None)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                temp = l1.val + carry
                carry = 0
                if temp > 9:
                    carry = 1 
                    temp -=10
                dummy.next = ListNode(temp, None)
                dummy = dummy.next
                l1 = l1.next

        if l2:
            while l2:
                temp = l2.val + carry
                carry = 0
                if temp > 9:
                    carry = 1 
                    temp -=10
                dummy.next = ListNode(temp, None)
                dummy = dummy.next
                l2 = l2.next

        if carry == 1:
            dummy.next = ListNode(1, None)
            
        return head.next