class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverse(root, res)
        return res
    
    def traverse(self, root, res):
        if root is not None:
            self.traverse(root.left, res)
            res.append(root.val)
            self.traverse(root.right, res)