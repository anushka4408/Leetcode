class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Convert int array to string and join
        new=[0]*len(num)
        for i in range(len(num)):
            new[i]=str(num[i])
        newstring=''.join(new)
        # convert ans back to sring and append in array after converting to int
        result=str(int(newstring)+k)
        newresult=[]
        for r in result:
            newresult.append(int(r))
        return newresult
