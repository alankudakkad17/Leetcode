class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first=None
        second=None
        perv=None

        def dfs(node):
            nonlocal first,second,perv
            if not node:
                return
            dfs(node.left)
            if perv and perv.val>node.val:
                if first is None:
                    first=perv
                second=node
            perv=node
            dfs(node.right)
        dfs(root)
        first.val,second.val=second.val,first.val
