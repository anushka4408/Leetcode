class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[0]*len(candies)
        greatest=max(candies)
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=greatest):
                result[i]=True
            else:
                result[i]=False
        return result
            

