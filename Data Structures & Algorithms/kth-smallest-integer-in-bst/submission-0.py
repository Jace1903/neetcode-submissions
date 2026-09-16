class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        result = [None]

        def inorder(node):
            if node is None or result[0] is not None:
                return
            inorder(node.left)
            if result[0] is not None:
                return
            count[0] += 1
            if count[0] == k:
                result[0] = node.val
                return
            inorder(node.right)

        inorder(root)
        return result[0]