class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows=[]
        column=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    rows.append(i)
                    column.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i in rows or j in column):
                    matrix[i][j]=0
        
            
        
        