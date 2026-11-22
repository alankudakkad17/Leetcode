from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        queue=deque([root])
        result=[]
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if i==size-1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return results
