class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        nword=list(word)
        ind=-1
        for i in range(len(nword)):
            if(nword[i]==ch):
                ind=i
                break
        
        new=[]
        for i in range(ind,-1,-1):
            new.append(nword[i])
        if(len(new)==0):
            return word
        nn=[]
        for i in range(ind+1,len(nword)):
            nn.append(nword[i])
        res=(''.join(new))+(''.join(nn))
        return res
        

        print(new)