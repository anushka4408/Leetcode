class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 5//2=2 range(1,3) result=[1,-1,2,-2,0]
        result=[]
        for i in range(1,n//2+1):
            result.append(i)
            result.append(-i)
        if(n%2 != 0):
            result.append(0)
        return result