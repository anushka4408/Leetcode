class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        res=0 
        dic={'M':1000,"D":500,'C':100,'L':50,'X':10,'V':5,'I':1}
        while i<len(s):
            if(i<len(s)-1 and dic[s[i+1]]>dic[s[i]]):
                res+=dic[s[i+1]]-dic[s[i]]
                i+=2
            else:
                res+=dic[s[i]]
                i+=1
        return res

        