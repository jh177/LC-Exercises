# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self._findLeaves(root, res)
        return res
        
    def _findLeaves(self, root, res):
        if not root: return 0
        
        left = self._findLeaves(root.left, res)
        right = self._findLeaves(root.right, res)
        level = max(left, right) + 1
        
        if level > len(res):
            res.append([])
        res[level-1].append(root.val)
        
        return level