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
# example 1
# [[1,3],[2,6],[8,10],[15,18]]
# res=[1,3]  i=2,6 (3>2)
# 3>2 and 3<6 res[-1][1]==6 res=[1,6]
# i=8,10 6<8 res=[1.6 , 8.10]
# i=15,18 10<15 res=[1.6 ,8.10 ,15.18]

# example2
# [[1,4] [2,3]]
# res=[1,4] i=2,3
# 4>2
# 4>2 and 4>3 continue res=[1,4]

