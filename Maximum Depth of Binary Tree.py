class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node,currdepth):
            if not node:
                return currdepth
            left=dfs(node.left,currdepth+1)
            right=dfs(node.right,currdepth+1)
            return max(left,right)
        return dfs(root,0)
