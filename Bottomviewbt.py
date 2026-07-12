'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
        queue=deque([(root,0)])
        
        hd_map={}
        while queue:
            node, hd=queue.popleft()
            hd_map[hd]=node.data
            if node.left:
                queue.append((node.left,hd-1))
            if node.right:
                queue.append((node.right,hd+1))
        return [hd_map[x] for x in sorted(hd_map)]
            
