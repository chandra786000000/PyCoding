class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root==None:
            return False
        if root.left==None and root.right==None and targetSum==root.val:
            return True
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)