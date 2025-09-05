# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def inorder(root,depth):
            if not root:
                return depth
            return max(inorder(root.left,depth+1),inorder(root.right,depth+1))
        return inorder(root,0)

        