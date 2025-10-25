from collections import defaultdict
from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):

        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # # window of size length p
        # # sort p and s and then compare.
        # m=len(p)
        # p=sorted(p)
        # output=[]
        # for i in range(len(s)-m+1):
        #     currwindow=s[i:i+m]
        #     currwindow=sorted(currwindow)
        #     if(currwindow==p):
        #         output.append(i)
        #     i+=1
        # return output

        # window of size p
        # hashmap to keep count of chars
        pdict=defaultdict(int)
        windowdict=defaultdict(int)
        m=len(p)

        for i in p:
            pdict[i]+=1
        for i in s[:m]:
            windowdict[i]+=1
        output=[]
        if(windowdict==pdict):
            output.append(0)
        for i in range(m,len(s)):
            # insert new ch
            windowdict[s[i]]+=1
            # remove old char
            windowdict[s[i-m]]-=1
            if(windowdict[s[i-m]]==0):
                del windowdict[s[i-m]]
            # check
            if windowdict==pdict:
                output.append(i-m+1)
        return output

            
