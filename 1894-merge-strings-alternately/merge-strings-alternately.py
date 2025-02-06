class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res=[]
        last=[]
        if(len(word1)>len(word2)):
            for i in range(len(word2)):
                res.append(word1[i])
                res.append(word2[i])
            last.append(word1[len(word2):len(word1)])
        else:
            for i in range(len(word1)):
                res.append(word1[i])
                res.append(word2[i])
            last.append(word2[len(word1):len(word2)])
        res.extend(last)
        # n=(len(word1)+len(word2))
        # while k<n:
        # if(len(word1)>len(word2)):
        #     for i in range(len(word2)):
        #         res.append(word1[i])
        #         res.append(word2[i])
        #     res.append(word1[(len(word1)-len(word2)):len(word1)])
        # elif(len(word1)<len(word2)):
        #     for i in range(len(word1)):
        #         res.append(word1[i])
        #         res.append(word2[i])
        #     res.append(word2[(len(word2)-len(word1)):len(word2)])
        # else:
        #     for i in range(len(word1)):
        #         res.append(word1[i])
        #         res.append(word2[i])

        return ''.join(res)




                

        
