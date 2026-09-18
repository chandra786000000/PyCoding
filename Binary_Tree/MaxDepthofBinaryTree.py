# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        left = 0
        right = 0
        if root.left:
            left =  1+self.maxDepth(root.left)
        if root.right:
            right = 1+self.maxDepth(root.right)
        return max(left,right)
        