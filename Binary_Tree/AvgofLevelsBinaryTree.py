# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            localSum = 0
            n = len(q)
            for _ in range(n):
                node= q.popleft()
                localSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(localSum/n)
        return ans
