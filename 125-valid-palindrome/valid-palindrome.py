class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new=[]
        for i in s:
            if(i.isalnum()):
                new.append(i.lower())
        res=''.join(new)
        if(res==res[::-1]):
            return True
        return False