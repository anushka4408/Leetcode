class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        j=0
        news=''
        while i<len(t) and j<len(s):
            if(s[j]==t[i]):
                news+=t[i]
                j+=1
            i+=1
        if(news!=s):
            return False
        return True
            