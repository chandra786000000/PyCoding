# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ansArr = []
    def traverseTree(self,tStr: str,root: TreeNode) -> int:
        if root.left is None and root.right is None:
            self.ansArr.append(tStr+str(root.val))
            return
        if root.left is not None:
            self.traverseTree(tStr+str(root.val),root.left)
        if root.right is not None:
            self.traverseTree(tStr+str(root.val),root.right)     
        return
    def sumNumbers(self, root: TreeNode | None) -> int:
        self.ansArr = []
        if root is None:
            return 0
        trackStr = ''
        self.traverseTree(trackStr,root)
        ans = 0
        for s in self.ansArr:
            ans += int(s)
        return ans