class Solution(object):
    def isAnagram(self, s, t):
        from collections import defaultdict
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        maped=defaultdict(int)
        for i in s:
            maped[i]+=1
        for i in t:
            if i not in maped:
                return False
            if i in maped and maped[i]==0:
                return False
            maped[i]-=1
        return True
        