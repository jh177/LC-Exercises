# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        
        res = []
        self.dfs(root, res)
                
        return res
        
        
    def dfs(self, node, res):
        if node is None:return
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        res.append(node.val)
        