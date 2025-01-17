class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        # an=2a+(n-1)*D
        # d=an-a/n-1
        d=arr[1]-arr[0]
        for i in range(len(arr)):
            if((arr[0]+(i)*d)!=arr[i]):
                return False
        return True
