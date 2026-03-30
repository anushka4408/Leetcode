class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if(len(s1)!= len(s2)):
            return False
        e1=sorted(s1[0::2])
        e2=sorted(s2[0::2])
        o1=sorted(s1[1::2])
        o2=sorted(s2[1::2])
        if(e1==e2 and o1==o2):
            return True
        return False
