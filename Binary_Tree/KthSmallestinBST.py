# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = None
    count = None
    k = 0;
    def traverse(self,root: Optional[TreeNode]):
        if root is None or self.k < 0:
            return

        self.traverse(root.left)
        if self.k is 1:
            self.ans = root.val
            self.k -= 1
            return
        self.k -=1
        self.traverse(root.right)
        return 

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.k = k
        self.ans = None
        self.traverse(root)
        return self.ans
        
        
"""
class Solution:
    build = []
    def traverse(self,root: Optional[TreeNode]):
        if root is None:
            return
        self.traverse(root.left)
        self.build.append(root.val)
        self.traverse(root.right)

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.build = []
        self.traverse(root)
        return self.build[k-1]
"""