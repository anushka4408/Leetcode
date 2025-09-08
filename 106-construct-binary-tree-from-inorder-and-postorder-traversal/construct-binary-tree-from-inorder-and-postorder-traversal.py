# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.postorderindex=len(postorder)-1
        inordermap={val:idx for idx,val in enumerate(inorder)}

        def helper(inleft,inright):
            if(inleft>inright):
                return None
            rootval=postorder[self.postorderindex]
            root=TreeNode(rootval)
            index=inordermap[rootval]
            self.postorderindex-=1
            root.right=helper(index+1,inright)
            root.left=helper(inleft,index-1)
            return root
        return helper(0,len(inorder)-1)
            

        