# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMax(self,root: Optional[TreeNode]) -> int:
        if root is None:
            return float('-inf')
        return max(root.val, max(self.getMax(root.left),self.getMax(root.right)))

    def getMin(self,root: Optional[TreeNode]) -> int:
        if root is None:
            return float('inf')
        return min(root.val, min(self.getMin(root.left),self.getMin(root.right)))

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return float('inf')
        left = float('inf')
        right = float('inf')
        if root.left:
            left = root.val - self.getMax(root.left)
        if root.right:
            right = self.getMin(root.right) - root.val
        return min(min(left,right),min(self.getMinimumDifference(root.left),self.getMinimumDifference(root.right)))
