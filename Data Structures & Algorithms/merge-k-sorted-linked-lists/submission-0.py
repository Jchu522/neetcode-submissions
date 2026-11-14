# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # push first element of each linked list into heap
        # with value of the node as the key and the
        # corresponding linked list index as the value
        # for the heap's entry

        # add the minimum element to the result and remove the element
        # from the top of the heap (heappop)
        
        # take the index of the linked list corresponding to the removed
        # element and push the linked list pointer forward to next,
        # if there is an element present add it to the heap under the 
        # same format and if there is no element then move forward

        # repeat until heap is empty, return compiled result

        # [1,3,4] 2
        # 1.next = 3
        # 3.next = 4

        # 1.next = 2
        # 2.next = 3

        h = []

        for l in lists:
            while l:
                h.append(l.val)
                l = l.next
        
        h.sort()
        res = ListNode()
        head = res

        for i in h:
            cur = ListNode(i)
            head.next = cur
            head = head.next

        return res.next
        