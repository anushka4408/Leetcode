# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def inorder(root):
            if not root:
                return []
            return inorder(root.left)+[root.val]+inorder(root.right)
        stack=inorder(root)
        # print(stack)
        absolute=float('inf')
        for i in range(1,len(stack)):
            prev=stack[i-1]
            absolute=min(absolute,abs(stack[i]-prev))
        return absolute
            
        