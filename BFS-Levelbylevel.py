# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrder(self, root):
        # code here\
        queue=deque([root])
        result=[]
        if not root:
            return []
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
