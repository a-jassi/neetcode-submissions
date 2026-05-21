# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            sum = (first + second + carry) % 10

            curr.next = ListNode(sum)

            carry = (first + second + carry) // 10

            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next

        

        

