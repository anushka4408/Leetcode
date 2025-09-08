# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        # """
        inordermap={val:idx for idx,val in enumerate(inorder)}
        self.preorderindex=0
        def helper(inleft,inright):
            if(inleft>inright):
                return None

            rootval=preorder[self.preorderindex]
            root=TreeNode(rootval)
            self.preorderindex+=1
            index=inordermap[rootval]
            root.left=helper(inleft,index-1)
            root.right=helper(index+1,inright)
            return root
        return helper(0,len(inorder)-1)


        # if not preorder:
        #     return None
        # rootval=preorder[0]
        # root=TreeNode(rootval)

        # indx=inorder.index(rootval)

        # leftinorder=inorder[:indx]
        # rightinorder=inorder[indx+1:]
        # leftsize=len(leftinorder)

        # leftpreorder=preorder[1:leftsize+1]
        # rightpreorder=preorder[leftsize+1:]

        # root.left=self.buildTree(leftpreorder,leftinorder)
        # root.right=self.buildTree(rightpreorder,rightinorder)
        # return root