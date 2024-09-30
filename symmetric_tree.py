from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_mirror(
        self, leftSub: Optional[TreeNode], rightSub: Optional[TreeNode]
    ) -> bool:
        if leftSub is None and rightSub is None:
            return True

        if leftSub is None or rightSub is None:
            return False

        return (
            leftSub.val == rightSub.val
            and self.is_mirror(leftSub.left, rightSub.right)
            and self.is_mirror(leftSub.right, rightSub.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.is_mirror(root.left, root.right)
