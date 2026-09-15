# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return
        if root.left is None and root.right is None:
            return True
        if root.right.val>root.val and root.left.val<root.val:
            return True
        return False
        