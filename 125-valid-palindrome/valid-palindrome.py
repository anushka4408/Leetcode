class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(left,right):
            if(left>right):
                return True
            if(res[left]!=res[right]):
                return False
            return check(left+1,right-1)

        new=[]
        for i in s:
            if(i.isalnum()):
                new.append(i.lower())
        res=''.join(new)
        return check(0,len(res)-1)
        
        # new=[]
        # for i in s:
        #     if(i.isalnum()):
        #         new.append(i.lower())
        # res=''.join(new)
        # if(res==res[::-1]):
        #     return True
        # return False