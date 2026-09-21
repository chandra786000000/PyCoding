# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self,root: Optional[TreeNode] , minRange: int, maxRange: int) -> bool:
        if root is None:
            return True

        if minRange < root.val and root.val < maxRange:
            return self.validate(root.left,minRange,root.val) and self.validate(root.right,root.val,maxRange)
        else: 
            return False
  
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        return self.validate(root.left,float('-inf'),root.val) and self.validate(root.right,root.val,float('inf'))
