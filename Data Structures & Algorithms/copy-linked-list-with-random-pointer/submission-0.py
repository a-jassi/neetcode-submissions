"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        nodeMap = {None: None}

        while curr:
            new = Node(curr.val)
            nodeMap[curr] = new
            curr = curr.next
        
        curr = head
        while curr:
            new = nodeMap[curr]
            new.next = nodeMap[curr.next]
            new.random = nodeMap[curr.random]
            curr = curr.next
        
        return nodeMap[head]
        
        

        
