# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root])
        height = 1
        while q:
            localAns = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                localAns.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if height % 2 == 0:
                localAns.reverse()
            ans.append(localAns)
            height += 1
        return ans
