# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    idx = 0
    store = {}
    def traverseInorder(self,start: int,end: int ,preorder: list[int],inorder: list[int]) -> Optional[TreeNode]:
        if start > end:
            return None
        inIdx = self.store[preorder[self.idx]]
        root = TreeNode(preorder[self.idx])
        self.idx +=1
        if start==end:
            return root
        root.left = self.traverseInorder(start,inIdx-1,preorder,inorder)
        root.right = self.traverseInorder(inIdx+1,end,preorder,inorder)
        return root


    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        self.store = {}
        if len(preorder)==0 or len(inorder)==0:
            return None
        n = len(preorder)
        for i in range(len(inorder)):
            self.store[inorder[i]] = i
        return self.traverseInorder(0,n-1,preorder,inorder)

# class Solution:
#     store = {}
#     def traverseInorder(self,preStart:int ,start: int,end: int ,preorder: list[int],inorder: list[int]) -> Optional[TreeNode]:
#         if start > end:
#             return None
#         inIdx = self.store[preorder[preStart]]
#         root = TreeNode(preorder[preStart])
#         if start==end:
#             return root
#         leftSize = inIdx - start
#         root.left = self.traverseInorder(preStart + 1 ,start,inIdx-1,preorder,inorder)
#         root.right = self.traverseInorder(preStart + 1 + leftSize,inIdx+1,end,preorder,inorder)
#         return root


#     def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
#         self.store = {}
#         if len(preorder)==0 or len(inorder)==0:
#             return None
#         n = len(preorder)
#         for i in range(len(inorder)):
#             self.store[inorder[i]] = i
#         return self.traverseInorder(0,0,n-1,preorder,inorder)
