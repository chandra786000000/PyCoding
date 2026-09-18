# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self,root: TreeNode | None) -> TreeNode | None:
        if root== None or (root.left == None and root.right == None):
            return root
        tmp = root.right
        root.right = root.left
        root.left = tmp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

    def sameTree(self, a: TreeNode | None, b: TreeNode | None) -> bool:
        if a==None and b==None:
            return True
        elif a==None or b==None:
            return False
        elif a.val == b.val and self.sameTree(a.left,b.left) and self.sameTree(a.right,b.right):
            return True
        else:
            return False
        
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root == None:
            return True
        if self.sameTree(root.left,self.invertTree(root.right)):
            return True
        return False
        