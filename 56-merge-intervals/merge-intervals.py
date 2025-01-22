class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if(len(res)==0 or res[-1][1]<intervals[i][0]):
                res.append(intervals[i])
            elif(res[-1][1]>=intervals[i][0]):
                if(res[-1][1]<=intervals[i][1]):
                    res[-1][1]=intervals[i][1]
                elif(res[-1][1]>=intervals[i][1]):
                    continue

            
        return res