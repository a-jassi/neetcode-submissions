# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size, curr = 0, head
        while curr:
            size += 1
            curr = curr.next
        
        if size - n == 0:
            return head.next

        curr = head
        i = 1
        while i != (size - n):
            curr = curr.next
            i += 1
        
        curr.next = curr.next.next
        return head
        
        


