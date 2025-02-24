class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top=0
        bottom=n-1
        left=0
        right=n-1
        matrix=[[0]*n for r in range(n)]
        count=1
        
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                matrix[top][i]=count
                count+=1
            top+=1
            for i in range(top,bottom+1):
                matrix[i][right]=count
                count+=1
            right-=1
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=count
                    count+=1
                bottom-=1
            if(left<=right):
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=count
                    count+=1
                left+=1

        return matrix

                