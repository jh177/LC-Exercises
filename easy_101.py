# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        
        return self._check(root.left, root.right)
    
    def _check(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self._check(left.right, right.left) and self._check(left.left, right.right)