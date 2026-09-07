class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            l.append(node.val)
            dfs(node.right)
            return l
        l=[]
        if not root:
            return []
        return dfs(root)
