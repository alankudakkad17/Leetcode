class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q=deque([root])
        while q:
            len_size=len(q)
            prev=None
            for _ in range(len_size):
                curr=q.popleft()
                if prev:
                    prev.next=curr
                prev=curr
                if(prev.left):
                    q.append(prev.left)
                if(prev.right):
                    q.append(prev.right)
        return root
