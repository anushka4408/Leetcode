class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        maxarea=0
        while left<right:
            width=right-left
            length=min(height[left],height[right])
            maxarea=max((width*length),maxarea)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxarea

        # maxarea=0
        # maxheight=0
        # for i in range(len(height)):
        #     maxheight=max(height[i],maxheight)
        #     for j in range(i+1,len(height)):
        #         maxarea=max((j-i)*(min(maxheight,height[j])),maxarea)
        # return maxarea
