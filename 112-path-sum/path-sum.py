# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if not root:
            return False
        
        stack = [(root, root.val)]  # store node and path sum so far
        
        while stack:
            node, s = stack.pop()
            
            # Check if leaf and sum matches
            if not node.left and not node.right and s == targetSum:
                return True
            
            if node.right:
                stack.append((node.right, s + node.right.val))
            if node.left:
                stack.append((node.left, s + node.left.val))
        
        return False


        # RECURSSION
        # if not root:
        #     return False
        # if(not root.left and not root.right):
        #     return root.val==targetSum
        # return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)

                

        