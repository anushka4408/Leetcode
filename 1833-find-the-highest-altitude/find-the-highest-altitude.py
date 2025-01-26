class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res=[]
        res.append(0)
        sum=0
        for i in gain:
            sum+=i
            res.append(sum)
        return max(res)